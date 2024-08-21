from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home page connected!</h1>')

def about(request):
    return HttpResponse('<p>Plan out your future game weeks for fantasy premier league.</p>')