from django.urls import path
from . import views

urlpatterns = [
    path("", views.rooms),
    path('<slug:slug>/', views.room, name='room')
]
