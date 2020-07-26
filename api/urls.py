from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet

router = DefaultRouter()
router.register(r'homes', HomeViewSet, basename='home')

urlpatterns = [
    re_path('^', include(router.urls)),
]