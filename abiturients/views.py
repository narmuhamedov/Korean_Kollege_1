from django.shortcuts import render
from main_page.models import ITCourses, Courses


def abituents_list(request):
    if request.method == "GET":
        courses = Courses.objects.all()
        itcourses = ITCourses.objects.all()
        context = {
            "courses": courses,
            "itcourses": itcourses,
        }
    return render(request, template_name='abit/abit_list.html', context=context)
