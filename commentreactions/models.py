from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment

# Create your models here.


class CommentReaction(models.Model):
    """
    CommentReaction model, related to
    'owner', i.e. a User instance who reacts to the comment,
    and 'comment', i.e. a Comment instance being reacted to.

    It tracks which comments are reacted to by which users
    and when the reaction occurred.
    Each user can only react to a comment once.
    Comment reactions are ordered by the most recent first.
    The __str__ method returns a string showing the user
    and the reacted comment.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment,
        related_name='commentreactions',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f'{self.owner} {self.comment}'
