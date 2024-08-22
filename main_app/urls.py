from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('teams/', views.teams_index, name='teams-index'),
     path('teams/<int:teams_id>/', views.teams_detail, name='teams-detail'),
]
