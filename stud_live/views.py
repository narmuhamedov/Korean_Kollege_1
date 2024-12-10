from django.shortcuts import render

def stud_live_list(request):
    if request.method == "GET":
        return render(request, template_name='stud_live.html')