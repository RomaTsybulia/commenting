from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from commenting import settings

def validate_file_size(value):
    if value.size > 1000000:  # 1000 KB
        raise ValidationError("File size exceeds the limit.")

def validate_image_dimensions(value):
    if value.width > 320 or value.height > 240:
        raise ValidationError("Image dimensions exceed the limit.")

class Author(AbstractUser):
    class Meta:
        verbose_name = "user"

    def __str__(self):
        return self.username


class Comment(models.Model):
    text = models.CharField(max_length=255)
    likes = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="author", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    main_comment = models.ForeignKey("self", on_delete=models.CASCADE,  blank=True, null=True)
    replies = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='reply',
        blank=True,
        null=True
    )
    head_comment = models.BooleanField(default=False)
    file = models.FileField(upload_to="files", null=True, blank=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.text}"


