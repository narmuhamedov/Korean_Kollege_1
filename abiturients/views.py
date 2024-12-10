from django.shortcuts import render
from main_page.models import ITCourses, Courses
from . import models



def abituents_list(request):
    if request.method == "GET":
        courses = Courses.objects.all()
        itcourses = ITCourses.objects.all()
        all_questions = models.AllQuestion.objects.all()
        edition_questions = models.EditionInformation.objects.all()
        context = {
            "courses": courses,
            "itcourses": itcourses,
            "all_questions": all_questions,
            "edition_questions": edition_questions,
        }
    return render(request, template_name='abit/abit_list.html', context=context)
