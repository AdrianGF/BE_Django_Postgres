from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectsViewSetAdmin
from .views import ProjectsPreviewSetAdmin
from django.conf.urls import include, url
# from . import views

router = DefaultRouter()
router.register('projects', ProjectsViewSetAdmin)

urlpatterns = [
    #/projects/
    url(r'', include(router.urls)),
]