from django.urls import path
from . import views

urlpatterns = [
    path('about_us/', views.about_view, name='about_us'),
    path('about_us_detail_aup/<int:id>/', views.about_aup_detail_view, name='about_detail_aup'),
    path('about_us_detail_ppc/<int:id>/', views.about_ppc_detail_view, name='about_detail_ppc'),
]