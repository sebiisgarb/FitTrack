from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, ExerciseViewSet, NutritionViewSet, WorkoutViewSet, WorkoutExerciseViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'nutrition', NutritionViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'workout-exercises', WorkoutExerciseViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]