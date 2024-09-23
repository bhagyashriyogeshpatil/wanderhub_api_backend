from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.

class SavedPost(models.Model):
    """
    SavedPost model, related to 
    'owner', i.e. a User instance who saves the post, 
    and 'post', i.e. a Post instance being saved.

    It tracks which posts are saved by which users 
    and when the save action occurred.
    Each user can only save a post once. 
    Saved posts are ordered by the most recent first. 
    The __str__ method returns a string showing the user
    and the saved post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name='savedposts',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'

