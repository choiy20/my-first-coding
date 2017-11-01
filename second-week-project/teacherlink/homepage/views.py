# from django.http import HttpResponse
from django.shortcuts import render
from .models import Course
# Create your views here.

def index(request):
    # return HttpResponse("Hello, students! You're at Teacher Link.")
    # return render (request, "index.html", {})
    course_list = Course.objects.all()
    ctx = {
        "course_list" : course_list
    }
    return render(request, "index.html", ctx)
