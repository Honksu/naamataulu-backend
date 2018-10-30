from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, enroll_recognize_test

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/', enroll_recognize_test, name='enroll_recognize_test')
]