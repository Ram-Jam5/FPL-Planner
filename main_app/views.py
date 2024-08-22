from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home page connected!</h1>')

def about(request):
    return render(request, 'about.html')

def teams_index(request):
    return render(request, 'teams/index.html', { 'teams':teams })

class Team:
    def __init__(self, name, goalkeeper ,defender1, defender2, defender3, defender4, midfielder1, midfielder2, midfielder3, forward1, forward2, forward3):
        self.name = name
        self.goalkeeper = goalkeeper
        self.defender1 = defender1
        self.defender2 = defender2
        self.defender3 = defender3
        self.defender4 = defender4
        self.midfielder1 = midfielder1
        self.midfielder2 = midfielder2
        self.midfielder3 = midfielder3
        self.forward1 = forward1
        self.forward2 = forward2
        self.forward3 = forward3
        
teams = [
    Team('Team 1', 'Vicarrio', 'Van Dijk', 'Alexander-Arnold', 'Pedro Porro', 'Saliba', 'Kevin De Bruyne', 'Bruno Fernandes', 'Cole Palmer', 'Erling Haaland', 'Alexander Isak', 'Ivan Toney'),
    Team('Team 2', 'Martinez', 'Burn', 'Alexander-Arnold', 'Gvardiol', 'Pedro Porro', 'Jota', 'Salah', ' Saka', 'Isak', 'Wood', 'Haaland'),
]