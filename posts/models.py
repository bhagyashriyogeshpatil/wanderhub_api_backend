from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    It has a title, content, image, place, and region.
    The owner is the user who created the post.
    It records when the post was created and last updated.
    Posts are sorted by the newest ones first. 
    The __str__ method shows the post's ID and title.
    """
    REGION_CHOICES = [
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Africa', 'Africa'),
        ('Oceania', 'Oceania'),
        ('Antarctica', 'Antarctica'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_rr2m0f.jpg',
        blank=True
    )
    place = models.CharField(max_length=150, blank=False)
    region = models.CharField(
        max_length=50,
        choices=REGION_CHOICES,
        default='Europe',
        blank=False
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'