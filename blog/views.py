from django.shortcuts import render, HttpResponse

# Create your views here.
def helloview(request):
    if request.method == 'GET':
        return HttpResponse('hello')