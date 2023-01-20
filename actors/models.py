from django.db import models

# Create your models here.

class Actors(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField(null=True, blank=True)
    average_movie_reate = models.FloatField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Actors"
        verbose_name_plural = "Actors"
