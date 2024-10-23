from rest_framework import viewsets, status
from users.models import User
from exercices.models import Exercise
from nutrition.models import Nutrition
from workouts.models import Workout, WorkoutExercise
from .serializers import UserSerializer, ExerciseSerializer, NutritionSerializer, WorkoutSerializer, WorkoutExerciseSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.token import RefreshToken
from rest_framework.response import Response






class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)
            return refresh({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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