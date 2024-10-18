from rest_framework import viewsets
from users.models import User
from exercices.models import Exercise
from nutrition.models import Nutrition
from workouts.models import Workout, WorkoutExercise
from .serializers import UserSerializer, ExerciseSerializer, NutritionSerializer, WorkoutSerializer, WorkoutExerciseSerializer

# ViewSet for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet for Exercise
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# ViewSet for Nutrition
class NutritionViewSet(viewsets.ModelViewSet):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializer

# ViewSet for Workout
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# ViewSet for WorkoutExercise
class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExercise.objects.all()
    serializer_class = WorkoutExerciseSerializer