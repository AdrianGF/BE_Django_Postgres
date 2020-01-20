from django.urls import path
from . import views

urlpatterns = [
    #/projects/
    path('', views.projects, name='projects'),
    #/projects/1/
    path('<int:project_id>/', views.detail, name='detail'),
]