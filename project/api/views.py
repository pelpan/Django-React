from pydoc import allmethods
from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework import generics
from .models import Room
# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    allmethods = ['']

# Add a new view  -> QueryView
class RoomQuery(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer