from django.shortcuts import render
from . models import Room

# Create your views here.

def rooms(request):
  rooms = Room.objects.all()
  return render(request, 'room/rooms.html', { 'rooms':rooms })

def room(request,slug):
  room = Room.objects.get(slug=slug)
  return render(request, 'room/room.html') 