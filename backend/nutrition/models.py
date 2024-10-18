from django.db import models
from users.models import User
# Create your models here.

class Nutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=50)
    kcal = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.meal_type} for {self.user.username} on {self.date}'