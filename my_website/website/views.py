from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse

def home(request):
    return render(request, "website/base.html")

def contact(request):
    return render(request, "website/contact.html")

def testimonials(request):
    return render(request, "website/testimonials.html")

def projects(request):
    return render(request, "website/projects.html")

def photos(request):
    return render(request, "website/photos.html")

def blog(request):
    return render(request, "website/blog.html")