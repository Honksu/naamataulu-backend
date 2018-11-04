from .face_recognition_interface import FaceRecognitionInterface
from .face_recognition_template import FaceRecognitionTemplateImplementer
from .face_recognition_template import DlibFaceRecognition

from api.models import User
import numpy as np

class FaceRecognitionFacade:
    def __init__(self):
        self.tolerance = 0.6

        # Implementers listed here
        recognition_implementers = {
            'template': FaceRecognitionTemplateImplementer,
			'dlib': DlibFaceRecognition,
        }

        # Wrap implementers inside interface
        self.recognition_implementers = {}
        for key, implementer in recognition_implementers.items():
            self.recognition_implementers[key] = FaceRecognitionInterface(implementer)

    def enroll(self, faces, user, implementer):
        # Get features serialized to a string
        imp = self.recognition_implementers[implementer]
        features = imp.get_features(faces)

        # Write features and implementer to user
		
        vector = np.array2string(features, separator=' ')
        user.face_features = vector
        user.face_recognition_implementer = implementer
        user.save()

    # Returns Django user
    def recognize(self, face):
        
        user_certainty_tuples = []

        # Go through all implementers
        for key, implementer in self.recognition_implementers.items():
            #print(str(implementer))
            # Filter users using given implementer
            users_with_implementer = User.objects.filter(face_recognition_implementer=key).all()
            # Get features of face to be recognized using implementer
            features = implementer.get_features(face)
            #print(features)
            # Get certainty that face is user's for all user using
            # the implementer
            for user in users_with_implementer:
                #print(user.face_features)
                distance = implementer.is_face(features, user.face_features)
                user_certainty_tuples.append((user, distance))

        # Sort the certainties
        user_distance_tuples = sorted(user_certainty_tuples, key= lambda tup: tup[1], reverse=False)
        
        # Most probable match
		
        match_user, match_distance = user_distance_tuples[0]
        
        # If match meets the tolerance, return match
        if match_distance <= self.tolerance:
            return match_user
        else:
            return None