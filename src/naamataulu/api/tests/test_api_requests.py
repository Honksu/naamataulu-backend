import os
import glob
from random import shuffle

from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, RequestsClient

from api.models import User
from api.views import UserViewSet

class UserTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        User.objects.create(username='Markku')

    def test_user_exists_list(self):
        request = self.factory.get('/api/v1/users')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.data[0]['username'], 'Markku')

    def test_user_exists(self):
        request = self.factory.get('/api/v1/users/1')
        view = UserViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.assertEqual(response.data['username'], 'Markku')

    def test_user_enroll(self):
        face_dir = os.path.join('api', 'tests', 'faces', '*.jpg')
        faces = glob.glob(face_dir)

        with open(faces[0]), 'rb') as data:
            request = self.factory.post('/api/v1/users/1', {'faces': data}, format='multipart')
            view = UserViewSet.as_view({'post': 'enroll'})
            response = view(request, pk=1)
            self.assertEqual(response.status_code, 200)

        shuffle(faces)

        faces = faces[:100]

        false_negatives = 0
        false_positives = 0
        successful = 0
        not_recognized = 0
        no_face = 0

        no_face_imgs = []
        not_recognized_imgs = []

        for face in faces:
            with open(face, 'rb') as data:
                request = self.factory.post('/api/v1/users', {'faces': data}, format='multipart')
                view = UserViewSet.as_view({'post': 'recognize'})
                try:
                    response = view(request)
                    if response.status_code == 200:
                        if response.data['id'] == 1:
                            successful += 1
                        else:
                            false_positives += 1
                    else:   
                        false_negatives += 1
                        not_recognized += 1
                        not_recognized_imgs.append(face)

                except IndexError:
                    false_negatives += 1
                    no_face += 1
                    no_face_imgs.append(face)
                
        print('False negatives: %s' % false_negatives)
        print('False positives: %s' % false_positives)
        print('Successful: %s' % successful)
        print('Total: %s' % len(faces))
        print('Not recognized: %s, No faces detected: %s' % (not_recognized, no_face))

        print('Not recognized: %s' % not_recognized_imgs)
        print('No face: %s' % no_face_imgs)