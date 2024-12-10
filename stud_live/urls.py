from django.urls import path
from . import views

urlpatterns = [
  path('stud_live/', views.stud_page_view, name='stud_live_list'),
  path('stud_live/<int:id>/', views.stud_page_detail_view, name='stud_live_list'),
]