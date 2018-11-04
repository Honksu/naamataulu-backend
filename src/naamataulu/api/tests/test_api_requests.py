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
        print(User.objects.all())
        request = self.factory.post('/api/v1/users/1')
        view = UserViewSet.as_view({'post': 'enroll'})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)