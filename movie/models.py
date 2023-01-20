from django.db import models
from helpers.image_paths import movie_image_path

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=155)
    year = models.IntegerField()
    rate = models.FloatField()
    duration = models.FloatField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=movie_image_path, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
