from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola Mundo!")

def index_v1(request):
    return HttpResponse("Hola Mundo V1!")