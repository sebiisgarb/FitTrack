from django.db import models
from workouts.models import Workout
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    fitness_level = models.CharField(max_length=15)
    created_ad = models.DateTimeField(auto_now=True)
    workout = models.ManyToManyField(Workout, verbose_name='workouts')


    def __str__(self):
        return self.username