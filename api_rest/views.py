from django.shortcuts import render
from .serializer import BebidaSerializer
from .models import Bebida
from rest_framework import viewsets

# Create your views here.
class BebidaViewset(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class= BebidaSerializer