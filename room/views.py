from django.shortcuts import render

# Create your views here.

def rooms(request):
  return render(request, 'room/rooms.html')