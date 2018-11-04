from django.test import TestCase
from api.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Markku")

    def test_user_exists(self):
        user = User.objects.get(username="Markku")
        self.assertEqual(user.username, "Markku")
