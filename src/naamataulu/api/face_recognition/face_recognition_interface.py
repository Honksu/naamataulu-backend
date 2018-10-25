class FaceRecognitionInterface:
    def __init__(self, imp):
        self.imp = imp # Implementing class

    # Return features in string format to be stored in database
    def get_features(self, faces):
        return self.imp.get_features(faces)

    # Returns probability that compared features match the given feature
    # 0.0 -> 1.0
    def is_face(self, features, compared_features):
        return self.imp.is_face(features, compared_features)