from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class ProfileListViewTests(APITestCase):
    """
    Profile creation upon registration, listing
    all profiles tests.
    """
    def setUp(self):
        bhagyashri = User.objects.create_user(
            username='bhagyashri', password='testpassword')
        yogesh = User.objects.create_user(
            username='yogesh', password='testpassword')
        shri = User.objects.create_user(
            username='shri', password='testpassword')

    def test_profile_created_on_user_registration(self):
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 3)

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)