from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    #path('projects/', views.home, name='projects'),
    path('project/<str:name>/', views.project, name='project'),
    #path('project/arcade/', views.arcade, name='arcade'),
]
