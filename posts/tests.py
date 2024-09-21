from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.


class PostListViewTests(APITestCase):
    """
    Tests for Post list view.
    Test user can create post and list all posts.
    """
    def setUp(self):
        User.objects.create_user(
            username='bhagyashri', password='testpassword')

    def test_can_list_posts(self):
        bhagyashri = User.objects.get(username='bhagyashri')
        Post.objects.create(owner=bhagyashri, title='test post title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='bhagyashri', password='testpassword')
        response = self.client.post('/posts/', {
            'title': 'test post title',
            'content': 'This is a test post.',
            'place': 'test place'})
        print(response.data) 
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/',{'title': 'post title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)