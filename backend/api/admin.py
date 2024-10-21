from django.contrib import admin
from users.models import UserProfile
from exercices.models import Exercise
from nutrition.models import Nutrition
from workouts.models import Workout, WorkoutExercise

# Register the models in the admin panel

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user',]  # Fields to display in the admin list view
    search_fields = ['user__username']  # Add search functionality

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  # Fields to display in the admin list view
    search_fields = ['name']

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'meal_type', 'kcal', 'protein', 'fats', 'carbs', 'date']
    search_fields = ['user__username', 'meal_type']  # Add search functionality

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'workout', 'exercise', 'sets', 'reps', 'rest_time']
    search_fields = ['workout__name', 'exercise__name']