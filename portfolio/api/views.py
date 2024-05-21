from django.shortcuts import render
from rest_framework import viewsets

from .models import Project, ProjectImage, Tag, Timeline
from .serializers import (
    ProjectImageSerializer,
    ProjectSerializer,
    TagSerializer,
    TimelineSerializer,
)


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
