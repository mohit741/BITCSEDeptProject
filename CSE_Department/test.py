from django.test import TestCase
from django.contrib.auth import get_user_model
from . import models


class TestProfileModel(TestCase):
    def test_profile_creation(self):
        User = get_user_model()
        user = User.objects.create(
            username="cs10001", password="django12345"
        )
        self.assertIsInstance(user.Profile, models.Profile)
        user.save()
        print(user.username)
        print(user.Profile)
        print(user.Profile.phone)
        self.assertIsInstance(user.Profile, models.Profile)
