from django.urls import path
from . import views

urlpatterns = [
    path('about_us/', views.about_view, name='about_us'),
]