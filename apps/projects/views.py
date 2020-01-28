from rest_framework import viewsets, generics
# from django.shortcuts import render
# from django.http import HttpResponse
from .models import Projects
from apps.projects.serializers import ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ProjectsViewSetAdmin(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ProjectsPreviewSetAdmin(generics.RetrieveAPIView):
    queryset = Projects.objects.all()

    def retrieve(self, request, pk):
        serializer_context = {'request': request}

        serializer_instance = self.queryset.get(pk=pk)

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
