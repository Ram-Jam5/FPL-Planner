from django.urls import path
from . import views

urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('about/', views.about, name='about'),
     path('teams/', views.teams_index, name='teams-index'),
     path('teams/<int:teams_id>/', views.teams_detail, name='teams-detail'),
     path('teams/create/', views.TeamsCreate.as_view(), name='teams-create'),
     path('teams/<int:pk>/update/', views.TeamsUpdate.as_view(), name='teams-update'),
     path('teams/<int:pk>/delete/', views.TeamsDelete.as_view(), name='teams-delete'),
     path('accounts/signup/', views.signup, name='signup'),
]
