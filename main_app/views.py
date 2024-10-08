from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import  Team, GOALKEEPERS, DEFENDERS, MIDFIELDERS, FORWARDS
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm


# Create your views here.


def about(request):
    return render(request, 'about.html')

@login_required
def teams_index(request):
    teams = request.user.team_set.all()
    goalkeepers = [goalkeeper[1] for goalkeeper in GOALKEEPERS]
    defenders = [defender[1] for defender in DEFENDERS]
    midfielders = [midfielder[1] for midfielder in MIDFIELDERS]
    forwards = [forward[1] for forward in FORWARDS]
    return render(request, 'teams/index.html', { 'teams':teams, 'goalkeepers':goalkeepers, 'defenders':defenders, 'midfielders':midfielders, 'forwards':forwards })

@login_required
def teams_detail(request, teams_id):
    team = Team.objects.get(id=teams_id)
    return render(request, 'teams/detail.html', {'team':team})

class TeamsCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = ['name', 'goalkeeper','defender1', 'defender2', 'defender3', 'defender4', 'midfielder1', 'midfielder2', 'midfielder3', 'forward1', 'forward2', 'forward3']
    success_url = '/teams/' 
    
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)      
    
class TeamsUpdate(LoginRequiredMixin, UpdateView):
    model=Team
    fields=['name', 'goalkeeper','defender1', 'defender2', 'defender3', 'defender4', 'midfielder1', 'midfielder2', 'midfielder3', 'forward1', 'forward2', 'forward3']
    
class TeamsDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url='/teams'
    
class Home(LoginView):
    template_name = 'home.html'
    
class SignUp(CreateView):
    form_class = RegisterForm
    template_name = "signup.html"
    success_url='/teams'
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super().form_valid(form)
    
# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('teams-index')
#         else:
#             error_message = 'Invalid sign up - try again'
#     form = UserCreationForm()
#     context = { 'form': form, 'error_message':error_message}
#     return render(request, 'signup.html', context)