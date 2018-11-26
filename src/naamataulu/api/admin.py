from django.contrib import admin

from api.models import User, FaceFeatures

# Register your models here.
admin.site.register(User)
admin.site.register(FaceFeatures)