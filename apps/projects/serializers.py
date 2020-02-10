from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    
    class Meta:
        model = Projects
        fields = ['slug', 'title', 'description', 'img', 'financed', 'pub_date']

