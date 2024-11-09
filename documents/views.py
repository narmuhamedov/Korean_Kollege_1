from django.shortcuts import render, get_object_or_404
from . import models


def documents(request):
    if request.method == 'GET':
        return render(request, 'documents.html')


def documents_license_view(request):
    if request.method == 'GET':
        license_ = models.License.objects.filter().order_by('-id')
        context = {'license_': license_}
        return render(request, template_name='documents/license/license.html', context=context)


def documents_organization_structure_view(request):
    if request.method == 'GET':
        structure_ = models.Organizational_structure.objects.filter().order_by('-id')
        context = {'structure_': structure_}
        return render(request, template_name='documents/structure_org/structure.html', context=context)


def documents_act_list_view(request):
    if request.method == 'GET':
        act_list = models.Normative_legal_acts.objects.filter().order_by('-id')
        context = {'act_list': act_list}
        return render(request, template_name='documents/normative_acts/documents_act.html'
                      , context=context)


def documents_act_detail_view(request, id):
    if request.method == 'GET':
        act_detail = get_object_or_404(models.Normative_legal_acts, id=id)
        context = {'act_detail': act_detail}
        return render(request, template_name='documents/normative_acts/documents_act_detail.html',
                      context=context)
