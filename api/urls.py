from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User
from .views import UserViewSet, HelloAPI
from rest_framework import routers, serializers, viewsets
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('hello/', HelloAPI),
]
