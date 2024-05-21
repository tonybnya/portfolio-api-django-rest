from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectImageViewSet, ProjectViewSet, TagViewSet, TimelineViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"tags", TagViewSet)
router.register(r"projectsimages", ProjectImageViewSet)
router.register(r"timelines", TimelineViewSet)

urlpatterns = [path("", include(router.urls))]
