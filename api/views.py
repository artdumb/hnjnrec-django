from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api.serializer import UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Students
from .serializer import StudentSerializer


@api_view(['GET'])
def HelloAPI(request):
    return Response("hello")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
