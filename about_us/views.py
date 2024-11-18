from django.shortcuts import render, get_object_or_404
from . import models

def about_view(request):
    if request.method == 'GET':
        about_t = models.About_Text.objects.all()
        about_aup = models.About_AUP.objects.all()
        about_ppc = models.About_PPC.objects.all()
        context = {
            'about_t': about_t,
            'about_aup': about_aup,
            'about_ppc': about_ppc,
        }
        return render(request, template_name='about.html', context=context)

def about_aup_detail_view(request, id):
    if request.method == 'GET':
        about_aup_detail = get_object_or_404(models.About_AUP, id=id)
        context = {
            'about_aup_detail': about_aup_detail,
        }
        return render(request, template_name='aboutDetail.html',
                      context=context)

def about_ppc_detail_view(request, id):
    if request.method == 'GET':
        about_ppc_detail = get_object_or_404(models.About_PPC, id=id)
        context = {'about_ppc_detail': about_ppc_detail}
        return render(request, template_name='aboutDetail_ppc.html', context=context)