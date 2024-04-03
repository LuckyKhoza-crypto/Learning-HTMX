from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    updated_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(
        upload_to='media/images/post_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
