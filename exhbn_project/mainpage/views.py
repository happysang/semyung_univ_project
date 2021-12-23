from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html')

def allprofile(request):
    return render (request, 'allprofile.html')

def detailprofile(request):
    return render (request, 'detailprofile.html')