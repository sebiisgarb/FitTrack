from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def exercices(request):
    return HttpResponse('aici e lista cu ex sau ce vrem sa mai aratam')