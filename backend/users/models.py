from django.db import models
from workouts.models import Workout
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(auto_now_add=False, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fitness_level = models.CharField(max_length=15, null=True, blank=True)
    created_ad = models.DateTimeField(auto_now=True)
    workout = models.ManyToManyField(Workout, verbose_name='workouts')


    def __str__(self):
        return str(self.user.username)