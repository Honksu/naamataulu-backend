import random
import numpy as np
import dlib
import cv2

face_recognition = dlib.face_recognition_model_v1('./api/face_recognition/models/dlib_face_recognition_resnet_model_v1.dat')
face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('./api/face_recognition/models/shape_predictor_68_face_landmarks.dat')

class FaceRecognitionTemplateImplementer:
    def __init__(self):
        pass

    def __str__(self):
        return 'TemplateImplementer'

    def get_features(self, faces):
        return str(random.randint(0,10000))

    def is_face(self, feature, compared_features):
        return random.random()
		
class DlibFaceRecognition:
    def __init__(self):
        pass

    def __str__(self):
        return 'Dlib'

    def get_features(self, faces):
    
        target_face = faces[0]

        target_face = np.asarray(target_face)

        height = len(target_face[0])
        width = len(target_face[0][0])
        channels = len(target_face[0][0][0])

        image= np.reshape(target_face, (height, width, channels))
        cv2.imwrite("laervi.png", image)
        main_face = cv2.imread("laervi.png")

        UPSAMPLING_FACTOR = 0
        faces = [
            (face.height() * face.width(), shape_predictor(main_face, face))
            for face in face_detector(main_face, UPSAMPLING_FACTOR)
        ]


        faces = sorted(faces, reverse=True)
        det_face = faces[0]
        detected_face = det_face[1]
        face_vector = np.array(face_recognition.compute_face_descriptor(main_face, detected_face)).astype(float)
        return face_vector
        
        #return str(random.randint(0,10000))

    def is_face(self, feature, compared_features):
        
        #Converting the retrieved string from the database to array
        compared = compared_features.replace('[','')
        compared = compared.replace(']','')
        print(compared)
        comparison = []
        for x in compared.split(' '):
            string = x
            if (not string.isspace()) and (not(len(string)<2)):
                print(string)
                flotari = float(string)
                comparison.append(flotari)
                
        comp = np.array(comparison)
        comparison = np.array(comparison)
        #compared_features = np.array(compared_features)
        feature = np.array(list(feature))
        print(comp)
        print(feature)
        difference = np.subtract(feature, comp)
        distance = np.linalg.norm(difference, axis=None)
        print(distance)
        return distance

        #return random.random()