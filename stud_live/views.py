from django.db.models import F
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from . import models

def stud_page_view(request):
    if request.method == "GET":
        news_list = models.StudentLive.objects.all().order_by('-id')
        paginator = Paginator(news_list, 3)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)
        return render(
            request, template_name="stud_live/stud_live.html", context={"stud_live_list": page_obj}
        )


def stud_page_detail_view(request, id):
    if request.method == "GET":
        stud_id = get_object_or_404(models.StudentLive, id=id)
        # Проверяем, был ли пользователь уже на этой странице
        viewed_news = request.session.get("viewed_stud", [])
        if id not in viewed_news:
            # Увеличиваем количество просмотров
            stud_id.views = F("views") + 1
            stud_id.save()
            stud_id.refresh_from_db()

            # Сохраняем в сессии, что пользователь уже смотрел эту новость
            viewed_news.append(id)
            request.session["viewed_news"] = viewed_news
        context = {"stud_id": stud_id}
        return render(request, template_name="stud_live/stud_live_detail.html", context=context)
