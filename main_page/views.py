from django.shortcuts import render, get_object_or_404
from . import models


def main_page(request):
    if request.method == 'GET':
        course_list = models.Courses.objects.all()
        course_it = models.ITCourses.objects.all()
        logo_image = models.LogoImage.objects.all()
        advanced = models.Advanced.objects.all()
        welcome = models.Welcome.objects.all()
        contact = models.Contact.objects.all()
        context = {
            'course_it': course_it,
            'course_list': course_list,
            'logo_image': logo_image,
            'advanced': advanced,
            'welcome': welcome,
            'contact': contact,
        }
        return render(request, template_name='index.html', context=context)


def main_page_it_details(request, id):
    if request.method == 'GET':
        course_it_id = get_object_or_404(models.ITCourses, id=id)
        context = {
            'course_it_id': course_it_id,
        }
        return render(request, template_name='index_detail_it.html', context=context)


def main_page_courses_details(request, id):
    if request.method == 'GET':
        course_id = get_object_or_404(models.Courses, id=id)
        context = {
            'course_id': course_id,
        }
        return render(request, template_name='index_detail_courses.html', context=context)


def news_page_view(request):
    if request.method == 'GET':
        news_list = models.News.objects.all()
        return render(request, template_name='news.html', context={'news_list': news_list})