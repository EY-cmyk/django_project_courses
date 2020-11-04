from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Course
from django.urls import reverse

def index(request):
    latest_courses_list = Course.objects.order_by('-date_of_start')[:5]
    return render(request, 'courses/list.html', {'latest_courses_list' : latest_courses_list})

    
def courseview(request, course_id):
    try:  
        a = Course.objects.get( id = course_id)
    except:
        raise Http404("Курс не найден!")
    return render(request, 'courses/courseview.html', {'course' : a})

