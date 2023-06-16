from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    logo = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username


class Comment(models.Model):
    text = models.CharField(max_length=255)
    likes = models.IntegerField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_thread = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='threads',
        blank=True,
        null=True
    )
