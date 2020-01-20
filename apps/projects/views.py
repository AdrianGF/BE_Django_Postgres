from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse("Hello, world. You're at the projects test.")

def detail(request, project_id):
    return HttpResponse("Details project nº %s." % project_id)
