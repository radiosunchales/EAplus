from django.shortcuts import render
from usuario.models import Alta_usuarios
from .serializers import Alta_usuarios_Serializer
from rest_framework import viewsets

class Alta_usuarios_View(viewsets.ModelViewSet):
    queryset = Alta_usuarios.objects.all()
    serializer_class = Alta_usuarios_Serializer

