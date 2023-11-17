from django.urls import path
from . import views

urlpatterns = [
  path('', views.frontpage, name="frontpage"),
  path('signup/', views.sign_up, name='signup'),
]