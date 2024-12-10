from django.urls import path
from . import views

urlpatterns = [
  path('stud_live/', views.stud_live_list, name='stud_live_list'),
]