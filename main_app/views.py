from django.shortcuts import render
from django.http import HttpResponse
from .models import  Team

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home page connected!</h1>')

def about(request):
    return render(request, 'about.html')

def teams_index(request):
    teams = Team.objects.all() 
    return render(request, 'teams/index.html', { 'teams':teams })

def teams_detail(request, teams_id):
    team = Team.objects.get(id=teams_id)
    return render(request, 'teams/detail.html', {'team':team})