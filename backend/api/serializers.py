from rest_framework import serializers
from users.models import User
from exercices.models import Exercise
from nutrition.models import Nutrition
from workouts.models import Workout, WorkoutExercise

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = '__all__'