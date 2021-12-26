from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    return render (request, 'home.html')

def allprofile(request):
    return render (request, 'allprofile.html')

def detailprofile(request):
    return render (request, 'detailprofile.html')




def worksall(request): #all
    works = Work.objects.all()
    return render (request, 'works.html', {'works': works})

def works(request, wtype): #gd / ad / media
    new_wtype = Type.objects.get(wtype = wtype)
    works = Work.objects.filter(wtype = new_wtype)
    return render (request, 'works.html', {'works': works})

def work_detail(request, pk): # type1
    work = Work.objects.filter(pk=pk)
    return render (request, 'work_detail.html', {'work': work})

def work_detail2(request, pk): # type2
    work = Work.objects.filter(pk=pk)
    return render (request, 'work_detail2.html', {'work': work})