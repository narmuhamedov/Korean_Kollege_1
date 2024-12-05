from django.urls import path
from . import views

urlpatterns = [
    path("documents_kkc/", views.documents, name="documents"),
    path("documents_license/", views.documents_license_view, name="documents_license"),
    path(
        "documents_organization_structure/",
        views.documents_organization_structure_view,
        name="documents_structure",
    ),
    path(
        "documents_normative_acts_list/",
        views.documents_act_list_view,
        name="documents_act_list",
    ),
    path(
        "documents_normative_acts_list/<int:id>/",
        views.documents_act_detail_view,
        name="act_detail",
    ),
]
