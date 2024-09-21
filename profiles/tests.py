from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class ProfileListViewTests(APITestCase):
    """
    Tests for profile creation.
    Checking that profiles are created when users register.
    Listing all profiles.
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


class ProfileDetailViewTests(APITestCase):
    """
    ProfileDetail view tests. 
    Getting profiles by valid and invalid IDs.
    Updating own profiles.
    Preventing updates to others' profiles.
    Ensuring profiles cannot be deleted.
    """
    def setUp(self):
        bhagyashri = User.objects.create_user(
            username='bhagyashri', password='testpassword')
        yogesh = User.objects.create_user(
            username='yogesh', password='testpasswordone')

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_profile(self):
        self.client.login(username='bhagyashri', password='testpassword')
        response = self.client.put(
            '/profiles/1/',
            {'name': 'bhagyashri'}
        )
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'bhagyashri')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cant_update_other_users_profile(self):
        self.client.login(username='yogesh', password='testpasswordone')
        response = self.client.put(
            '/profiles/1/', {'name': 'bhagyashri'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cant_delete_own_profile_authorised(self):
        self.client.login(username='bhagyashri', password='testpassword')
        response = self.client.delete('/profiles/1/')
        self.assertTrue(Profile.objects.filter(pk=1).exists())
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_user_cant_delete_other_users_profile(self):
        self.client.login(
            username='yogesh', password='testpasswordone')
        response = self.client.delete('/profiles/1/')
        self.assertTrue(Profile.objects.filter(pk=1).exists())
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)