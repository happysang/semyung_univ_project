from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render (request, 'home.html')

def allprofile(request):
    data_insert()
    allfile = Profile.objects.all()
    return render (request, 'allprofile.html', {'allfile':allfile})

def detailprofile(request,each_id):
    detail_obj = get_object_or_404(Profile, pk = each_id)
    return render (request, 'detailprofile.html', {'ppp':detail_obj})

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

##데이터 삽입



def data_insert():
    profile_list = []
    
    obj = Profile()
    obj.name = "김선식"
    obj.pimage = 'pimage/thum/김선식 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/김선식.jpg'
    obj.eng_name = "KIM, SEON-SIK"
    obj.email = "zmffhwld753@gmail.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "민경서"
    obj.pimage = 'pimage/thum/민경서 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/민경서.jpg'
    obj.eng_name = "MIN, KYOUNG-SEO"
    obj.email = "821z594@gmail.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김인학"
    obj.pimage = 'pimage/thum/김인학 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/김인학.jpg'
    obj.eng_name = "KIM, IN-HAK"
    obj.email = "mniac123@naver.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "박요한"
    obj.pimage = 'pimage/thum/박요한 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/박요한.jpg'
    obj.eng_name = "PARK, YO-HAN"
    obj.email = "yohanux@gmail.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "강민혁"
    obj.pimage = 'pimage/thum/강민혁 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/강민혁.jpg'
    obj.eng_name = "KANG, MIN-HYUK"
    obj.email = "minhyuk3308@naver.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "류호경"
    obj.pimage = 'pimage/thum/류호경 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/류호경.jpg'
    obj.eng_name = "RYU, HO-KYUNG"
    obj.email = "ryuhokyung9764@gmail.com"
    profile_list.append(obj)
        
    obj = Profile()
    obj.name = "정명현"
    obj.pimage = 'pimage/thum/정명현 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/정명현.jpg'
    obj.eng_name = "KIM, SEON-SIK"
    obj.email = "kih3957@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "박효정"
    obj.pimage = 'pimage/thum/박효정 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/박효정.jpg'
    obj.eng_name = "PARK, HYO-JEONG"
    obj.email = "qkrgywjd32@gmail.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "박주이"
    obj.pimage = 'pimage/thum/박주이 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/박주이.jpg'
    obj.eng_name = "PARK, JU-YI"
    obj.email = "5733wndl@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "원도윤"
    obj.pimage = 'pimage/thum/원도윤 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/원도윤.jpg'
    obj.eng_name = "WON, DO-YOON"
    obj.email = "do-hwazi@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "신혜현"
    obj.pimage = 'pimage/thum/신혜현 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/신혜현.jpg'
    obj.eng_name = "SHIN, HYE-HYEON"
    obj.email = "enffl22500@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "최현우"
    obj.pimage = 'pimage/thum/최현우 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/최현우.jpg'
    obj.eng_name = "CHOI, HYUN-WOO"
    obj.email = "alsguswns2@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "정지황"
    obj.pimage = 'pimage/thum/정지황 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/정지황.jpg'
    obj.eng_name = "JEONG, JI-HWANG"
    obj.email = "earth19999@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "최영현"
    obj.pimage = 'pimage/thum/최영현 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/최영현.jpg'
    obj.eng_name = "CHOI, YOUNG-HYEON"
    obj.email = "dudgusdl03@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "신진경"
    obj.pimage = 'pimage/thum/신진경 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/신진경.jpg'
    obj.eng_name = "SHIN, JIN-GYEONG"
    obj.email = "api0422@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김민서"
    obj.pimage = 'pimage/thum/김민서 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/김민서.jpg'
    obj.eng_name = "KIM, MIN-SEO"
    obj.email = "alstj6136@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김예지"
    obj.pimage = 'pimage/thum/김예지 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/김예지.jpg'
    obj.eng_name = "KIM, YE-JI"
    obj.email = "kkyj9846@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "전예린"
    obj.pimage = 'pimage/thum/전예린 썸네일.jpg'
    obj.d_pimage = 'pimage/detail/전예린.jpg'
    obj.eng_name = "JEON, YE-LIN"
    obj.email = "yxyxxyxxx@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김나영"
    obj.pimage = 'pimage/thum/김나영 썸네일.jpg'
    obj.eng_name = "KIM, NA-YOUNG"
    obj.email = "jme06050@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김예지"
    obj.pimage = 'pimage/thum/김예지 썸네일.jpg'
    obj.eng_name = "KIM, YE-JI"
    obj.email = "kkyj9846@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김다은"
    obj.pimage = 'pimage/thum/김다은 썸네일.jpg'
    obj.eng_name = "KIM, DA-EUN"
    obj.email = "daen0202@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "김영경"
    obj.pimage = 'pimage/thum/김영경 썸네일.jpg'
    obj.eng_name = "KIM, YOUNG-KYUNG"
    obj.email = "kim51867@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "안예은"
    obj.pimage = 'pimage/thum/안예은 썸네일.jpg'
    obj.eng_name = "AN, YE-EUN"
    obj.email = "0629an@naver.com"
    profile_list.append(obj)
    
    obj = Profile()
    obj.name = "정예림"
    obj.pimage = 'pimage/thum/정예림 썸네일.jpg'
    obj.eng_name = "JUNG, YE-LIM"
    obj.email = "ylimjung99@gmail.com"
    profile_list.append(obj)
    
    for x in profile_list:
        if Profile.objects.filter(name=x.name).exists(): #새로고침 시 중복체크
            pass
        else:
            x.save()