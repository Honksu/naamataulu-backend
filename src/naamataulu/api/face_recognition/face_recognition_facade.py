from face_recognition_interface import FaceRecognitionInterface
from face_recognition_template import FaceRecognitionTemplateImplementer

from .models import User

class FaceRecognitionFacade:
    def __init__(self, imp):
        self.tolerance = 0.9

        # Implementers listed here
        recognition_implementers = {
            'template': FaceRecognitionTemplateImplementer,
        }

        # Wrap implementers inside interface
        self.recognition_implementers = {}
        for key, implementer in recognition_implementers.items():
            self.recognition_implementers[key] = FaceRecognitionInterface(implementer)

    def enroll(faces, user, implementer):
        # Get features serialized to a string
        features = self.recognition_implementers[implementer].get_features(faces)

        # Write features and implementer to user
        user.face_features = features
        user.face_recognition_implementer = implementer
        user.save()

    # Returns Django user
    def recognize(face):
        
        user_certainty_tuples = []

        # Go through all implementers
        for key, implementer in recognition_implementers.items():
            # Filter users using given implementer
            users_with_implementer = User.objects
                .filter(face_recognition_implementer=implementer)
                .all()
            # Get features of face to be recognized using implementer
            features = implementer.get_features(face)

            # Get certainty that face is user's for all user using
            # the implementer
            for user in users_with_implementer:
                certainty = implementer.is_face(features, user.face_features)
                user_certainty_tuples.append(user, certainty)

        # Sort the certaintities
        user_certainty_tuples = sorted(user_certainty_tuples, key= lambda tup: tup[1], reverse=True)
        
        # Most probable match
        match_user, match_certainty = user_certainty_tuples[1]
        
        # If match meets the tolerance, return match
        if match_certainty >= self.tolerance:
            return match_user
        else:
            return user