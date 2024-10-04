from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Follower(models.Model):
    """
    Follower model, related to
    'owner', i.e. a User instance who is following,
    and 'followed', i.e. a User instance being followed.

    It tracks who is following whom and
    when the follow action happened.
    Each user can only follow another user once.
    Follows are ordered by the most recent first.
    The __str__ method returns a string showing both users.

    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
