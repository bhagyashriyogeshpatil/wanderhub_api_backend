from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    """
    Comment model, related to 'owner', i.e. a User instance, 
    and 'post', i.e. a Post instance.
    
    It records the content of the comment, the user who made it, 
    and the post it belongs to. 
    The model tracks when the comment was created and last updated. 
    Comments are sorted by the newest ones first. 
    The __str__ method returns the content of the comment.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.content