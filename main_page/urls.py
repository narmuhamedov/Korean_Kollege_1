from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home_page'),
    path('it_detail/<int:id>/', views.main_page_it_details, name='it_detail'),
    path('course_detail/<int:id>/', views.main_page_courses_details, name='course_detail'),
    path('news_list/', views.news_page_view, name='news_list'),
    path('news_list/<int:id>/', views.news_page_detail_view, name='news_detail'),
]