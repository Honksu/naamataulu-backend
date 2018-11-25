from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name =  models.CharField(max_length=64, null=True, blank=True)
    face_features = models.TextField(null=True, blank=True)
    face_recognition_implementer = models.CharField(null=True, max_length=64, blank=True)