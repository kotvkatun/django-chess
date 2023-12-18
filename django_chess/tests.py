from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class RegistrationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="test"
        )

    def test_user_model(self):
        self.assertEqual(self.user.username, "testuser")
