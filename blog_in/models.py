from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(verbose_name='event_images/')