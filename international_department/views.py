from django.shortcuts import render
from . import models


def information_international(request):
    if request.method == "GET":
        gallery = models.Gallery.objects.all().order_by("-id")
        employee = models.EmployeeDepartment.objects.all()
        short_information = models.ShortStoryDepartment.objects.all()
        general_information = models.GeneralInformation.objects.all()
        deparment_activity = models.DepartmentActivities.objects.all()
        regulary_document = models.RegulatoryDocuments.objects.all().order_by("-id")
        context = {
            "gallery": gallery,
            "employee": employee,
            "short_information": short_information,
            "general_information": general_information,
            "deparment_activity": deparment_activity,
            "regulary_document": regulary_document,
        }
    return render(
        request, template_name="internation/internation.html", context=context
    )
