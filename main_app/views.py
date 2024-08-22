from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class TeamsCreate(CreateView):
    model = Team
    fields = '__all__'
    success_url = '/teams/'
    
class TeamsUpdate(UpdateView):
    model=Team
    fields=['name', 'goalkeeper','defender1', 'defender2', 'defender3', 'defender4', 'midfielder1', 'midfielder2', 'midfielder3', 'forward1', 'forward2', 'forward3']
    
class TeamsDelete(DeleteView):
    model = Team
    success_url='/teams'