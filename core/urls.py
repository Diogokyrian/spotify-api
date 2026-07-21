from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SingerViewSet, AlbumViewSet

router = DefaultRouter()
router.register(r"singers", SingerViewSet, basename="singer")
router.register(r"albums", AlbumViewSet, basename="album")

urlpatterns = [
    path("", include(router.urls)),
]
