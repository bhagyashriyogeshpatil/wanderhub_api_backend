from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model, related to 'owner', i.e. a User instance.
    It contains a name, bio, and profile image for the user.
    The profile records when it was created and last updated.
    Profiles are sorted by the newest ones first.
    The __str__ method returns the owner's username and 's profile.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_t7e7o1.png'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
