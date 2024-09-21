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
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/',{'title': 'post title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    """
    Tests for Post detail views.
    Test retrieve, update and delete methods
    for authorised and unauthorised users.
    """
    def setUp(self):
        bhagyashri = User.objects.create_user(
            username='bhagyashri', password='testpassword')
        yogesh = User.objects.create_user(
            username='yogesh', password='testpassword')
        Post.objects.create(
            owner=bhagyashri, 
            title='test post title',
            content='bhagyashris post content'
        )
        Post.objects.create(
            owner=yogesh,
            title='another post title',
            content='yogeshs post content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'test post title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='bhagyashri', password='testpassword')
        response = self.client.put('/posts/1/', {
            'title': 'update test post title',
            'content': 'This is updated a test post.',
            'place': 'update test place'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'update test post title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_cant_update_another_users_post(self):
        self.client.login(username='bhagyashri', password='testpassword')
        response = self.client.put('/posts/2/', {
            'title': 'update test post title',
            'content': 'This is updated a test post.',
            'place': 'update test place'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_post_authorised(self):
        self.client.login(username='bhagyashri', password='testpassword')
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cant_delete_others_post_unauthorised(self):
        self.client.login(username='bhagyashri', password='testpassword')
        response = self.client.delete('/posts/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)