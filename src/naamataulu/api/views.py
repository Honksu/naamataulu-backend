from io import BufferedWriter, BytesIO

from rest_framework import viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.template import loader
from django.http import HttpResponse

import cv2
import numpy as np

from .serializers import UserSerializer
from .models import User

from .face_recognition.face_recognition_facade import FaceRecognitionFacade

DEFAULT_IMPLEMENTER = 'dlib' # TODO this to database?

# Testing view for enrollment and recognition
def enroll_recognize_test(request):
        template = loader.get_template('api/enroll_recognize_test.html')
        return HttpResponse(template.render({}, request))

# Returns numpy array of image file
def requestFaceToNp(request_faces):
        np_faces = []
        for face in request_faces:
                print(face)
                face_bytes = np.asarray(bytearray(face.read()), dtype=np.uint8)
                np_faces.append(cv2.imdecode(face_bytes, cv2.IMREAD_COLOR))
        
        print(len(np_faces))            # N images
        print(len(np_faces[0]))         # Image height
        print(len(np_faces[0][0]))      # Image width
        print(len(np_faces[0][0][0]))   # N channels
        
        return np_faces

class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        permission_classes = (IsAuthenticated,)

        @action(detail=True, methods=['post'])
        @parser_classes((MultiPartParser,))
        def enroll(self, request, pk=None):
                faces_upload = request.FILES.getlist('faces')
                faces = requestFaceToNp(faces_upload)
                f = FaceRecognitionFacade()
                f.enroll([faces], User.objects.get(pk=pk), DEFAULT_IMPLEMENTER)
                return Response('Enrollment successful')

        @action(detail=False, methods=['post'])
        @parser_classes((MultiPartParser,))
        def recognize(self, request):
                faces_upload = request.FILES.getlist('faces')
                faces = requestFaceToNp(faces_upload)
                f = FaceRecognitionFacade()
                user = f.recognize([faces])
                if user is None:
                        return Response('User not recognized', status=404)
                else:
                        serializer = self.get_serializer(user, many=False)
                        return Response(serializer.data)