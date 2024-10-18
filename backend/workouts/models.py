from django.db import models
from exercices.models import Exercise
# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length=50)  
    type = models.CharField(max_length=20)
    description = models.TextField()
    duration = models.IntegerField()
    difficulty_level = models.CharField(max_length=10)
    exercices = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField()

    def __str__(self):
        return f'{self.workout} - {self.exercise} ({self.sets} sets, {self.reps} reps)'