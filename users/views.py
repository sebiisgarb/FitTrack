from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def users(request):
    return HttpResponse('aici userii')