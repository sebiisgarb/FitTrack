from rest_framework import serializers # type: ignore
from users.models import UserProfile
from exercices.models import Exercise
from nutrition.models import Nutrition
from workouts.models import Workout, WorkoutExercise
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user =  authenticate(username=username, password=password)
            if user in None:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Must include username and password')
        
        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
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