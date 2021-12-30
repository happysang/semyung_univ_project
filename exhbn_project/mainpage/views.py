from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render (request, 'home.html')


def allprofile(request):
    data_insert()
    allfile = Profile.objects.all()
    return render (request, 'allprofile.html', {'allfile':allfile})

def detailprofile(request):
    return render (request, 'detailprofile.html')

def about(request):
    return render (request, 'about.html')

def worksall(request): #all
    works = Work.objects.all()
    return render (request, 'works.html', {'works': works})

def works(request, wtype): #gd / ad / media
    new_wtype = Type.objects.get(wtype = wtype)
    works = Work.objects.filter(wtype = new_wtype)
    return render (request, 'works.html', {'works': works})

def work_detail(request, pk): # type1 광고 디자인 ad type2 영상 애니메이션 me type3 그래픽 디자인 gr
    work = Work.objects.filter(pk=pk)
    wtypeObj = Type.objects.get(wtype = work[0].wtype)
    print(wtypeObj)
    wtypeStr = wtypeObj.wtype # ad / me / gr
    print("wtypeStr: "+wtypeStr)
    if wtypeStr == 'ad':
        return render (request, 'work_detail.html', {'work': work})
    elif wtypeStr == 'me':
        return render (request, 'work_detail2.html', {'work': work})
    elif wtypeStr == 'gr':
        return render (request, 'work_detail3.html', {'work': work})

def work_detail_static(request):
    return render(request, 'work_detail_static.html')

def work_detail2_static(request):
    return render(request, 'work_detail2_static.html')

def work_detail3_static(request):
    return render(request, 'work_detail3_static.html')   





def data_insert():
    profile_list = []
    
    obj = Profile()
    obj.name = "김선식"
    obj.pimage = 'pimage/thum/김선식 썸네일.jpg'
    obj.eng_name = "KIM, SEON-SIK"
    obj.email = "zmffhwld753@gmail.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "민경서"
    obj.pimage = 'pimage/thum/민경서 썸네일.jpg'
    obj.eng_name = "MIN, KYOUNG-SEO"
    obj.email = "821z594@gmail.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김인학"
    obj.pimage = 'pimage/thum/김인학 썸네일.jpg'
    obj.eng_name = "KIM, IN-HAK"
    obj.email = "mniac123@naver.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "박요한"
    obj.pimage = 'pimage/thum/박요한 썸네일.jpg'
    obj.eng_name = "PARK, YO-HAN"
    obj.email = "yohanux@gmail.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "강민혁"
    obj.pimage = 'pimage/thum/강민혁 썸네일.jpg'
    obj.eng_name = "KANG, MIN-HYUK"
    obj.email = "minhyuk3308@naver.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "류호경"
    obj.pimage = 'pimage/thum/류호경 썸네일.jpg'
    obj.eng_name = "RYU, HO-KYUNG"
    obj.email = "ryuhokyung9764@gmail.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "정명현"
    obj.pimage = 'pimage/thum/정명현 썸네일.jpg'
    obj.eng_name = "KIM, SEON-SIK"
    obj.email = "kih3957@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "박효정"
    obj.pimage = 'pimage/thum/박효정 썸네일.jpg'
    obj.eng_name = "PARK, HYO-JEONG"
    obj.email = "qkrgywjd32@gmail.com"
    profile_list.append(obj)
    
    
    
    
    
    
    
    
    for x in profile_list:
        if Profile.objects.filter(name=x.name).exists(): #새로고침 시 중복체크
            pass
        else:
            x.save()