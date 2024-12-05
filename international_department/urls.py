from django.urls import path
from . import views

urlpatterns = [
    path(
        "international_department/",
        views.information_international,
        name="international_department",
    ),
]
