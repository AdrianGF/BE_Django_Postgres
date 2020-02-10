from rest_framework import viewsets, generics, mixins
from .models import Projects
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.projects.serializers import ProjectSerializer
# from django.shortcuts import render
# from django.http import HttpResponse

class ProjectListView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'