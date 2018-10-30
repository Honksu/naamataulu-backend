import random

class FaceRecognitionTemplateImplementer:
    def __init__(self):
        pass

    def __str__(self):
        return 'TemplateImplementer'

    def get_features(self, faces):
        return str(random.randint(0,10000))

    def is_face(self, feature, compared_features):
        return random.random()