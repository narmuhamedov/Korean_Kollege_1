from django.db.models import F
from django.core.paginator import Paginator
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
        mission = models.Mission.objects.all()
        open_door = models.OpenDoor.objects.all()
        news_list = models.News.objects.all().order_by('-id')
        paginator = Paginator(news_list, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        context = {
            'course_it': course_it,
            'course_list': course_list,
            'logo_image': logo_image,
            'advanced': advanced,
            'welcome': welcome,
            'contact': contact,
            'mission': mission,
            'open_door': open_door,
            'page_obj': page_obj,
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
        paginator = Paginator(news_list, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        return render(request, template_name='news.html', context={'page_obj': page_obj})

def news_page_detail_view(request, id):
    if request.method == 'GET':
        news_id = get_object_or_404(models.News, id=id)
        # Проверяем, был ли пользователь уже на этой странице
        viewed_news = request.session.get('viewed_news', [])
        if id not in viewed_news:
            # Увеличиваем количество просмотров
            news_id.views = F('views') + 1
            news_id.save()
            news_id.refresh_from_db()

            # Сохраняем в сессии, что пользователь уже смотрел эту новость
            viewed_news.append(id)
            request.session['viewed_news'] = viewed_news
        context = {'news_id': news_id}
        return render(request, template_name='newDetail.html', context=context)