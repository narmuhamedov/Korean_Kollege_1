from django.shortcuts import render
from . import models

def about_view(request):
    if request.method == 'GET':
        about_t = models.About_Text.objects.all()
        context = {'about_t': about_t}
        return render(request, template_name='about.html', context=context)