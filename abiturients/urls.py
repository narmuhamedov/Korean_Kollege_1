from django.urls import path
from . import views

urlpatterns = [
    path('abiturients/', views.abituents_list, name='abituents_list'),
]