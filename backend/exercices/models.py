from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50)
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name