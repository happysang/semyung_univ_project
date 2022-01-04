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

def init_data(request):
    type_insert()
    work_insert_ad()
    work_insert_gr()
    return render(request, 'home.html')


def type_insert():
    type_list = []
    t1 = Type()
    t1.wtype = 'ad'
    t2 = Type()
    t2.wtype = 'me'
    t3 = Type()
    t3.wtype = 'gr'
    type_list.append(t1)
    type_list.append(t2)
    type_list.append(t3)
    for t in type_list:
        if Type.objects.filter(wtype=t.wtype).exists(): #새로고침 시 중복체크
            pass
        else:
            t.save()

def work_insert_ad():
    work_list = []

    w = Work()
    w.artist='김선식'
    w.title= '유튜브붐'
    w.description= 'YOUTUBE의 정보량은 수류탄과 같이 엄청난 폭발력을 가지고 있다는 의미를 담았다.'
    w.thumbnail= 'wimage/thum/김선식_유튜브붐_-썸네일.jpg'
    w.pic= 'wimage/pic/김선식_유튜브붐_웹.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)
    
    w = Work()
    w.artist='민경서'
    w.title= '매운맛에 긴급처방, 숙취에 긴급투하'
    w.description= '매운 것을 먹어 입에 불이 나는 것 같을 때 바나나우유를 먹어 진정시키고, 술 먹은 다음날 숙취가 있을 때 바나나우유를 먹어 진정시켜주라는 것을 표현한 상품광고이다.'
    w.thumbnail= 'wimage/thum/민경서_매운맛에 긴급처방, 숙취에 긴급투하_썸네일.jpg'
    w.pic= 'wimage/pic/민경서_매운맛에 긴급처방, 숙취에 긴급투하.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist='민경서'
    w.title= '비타민C 저축왕'
    w.description= '돼지저금통에 동전을 채워 저축하듯이 비타민을 내 몸에 채워 저축하라는 의미하는 상품광고이다. '
    w.thumbnail= 'wimage/thum/민경서_비타민C 저축왕_썸네일.jpg'
    w.pic= 'wimage/pic/민경서_비타민C 저축왕.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist='민경서'
    w.title= '이케아에 꽂히다'
    w.description= '“이케아에 꽂히다”의 유사 발음인 꼬치를 사용해 이케아의 합리적인 가격의 가구들을 한 번에 꼬치에 꽂혀있는 모습을 표현한 기업광고이다.'
    w.thumbnail= 'wimage/thum/민경서_이케아에 꽂히다_썸네일.jpg'
    w.pic= 'wimage/pic/민경서_이케아에 꽂히다.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist='김인학'
    w.title= '밀어서 배송완료'
    w.description= '아이폰의 잠금 해제 UI를 활용하여 ‘FedEx’를 통한 해외 배송은 매우 쉽고 빠르다는 것을 표현한 작품이다.'
    w.thumbnail= 'wimage/thum/김인학_밀어서 배송완료_썸네일.jpg'
    w.pic= 'wimage/pic/김인학_밀어서 배송완료.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    for x in work_list:
        if Work.objects.filter(title=x.title).exists(): #새로고침 시 중복체크
            pass
        else:
            x.save()



def work_insert_gr():
    gr_list = []

    gr = Work()
    gr.artist='김선식'
    gr.title= 'People & pet'
    gr.description= '무분별한 분양과 무책임한 방치, 유기 때문에 고통을 받는 반려동물들이 많아지고 있다. 그러한 상황을 타파하기 위해서 반 려 동물 등록제와 연동 가능한 애플리케이션을 디자인하였다.'
    gr.thumbnail= 'gimage/thum/김선식_P_P_썸네일.jpg'
    gr.pic= 'gimage/pic/김선식_P_P.jpg'
    gr.picprd= 'gimage/picprd/김선식_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='민경서'
    gr.title= '캠핑 포레스트'
    gr.description= '캠핑은 계절과 관계없이 언제든 즐길 수 있는 활동이라는 것을 표현하고 계절별로 캠핑을 했을 때 느낄 수 있는 매력을 보 여주려 했다. 계절뿐만 아니라 밤과 낮, 새벽 시간에 따라 다른 매력과 활동들을 소개했다. 일러스트를 보며 바쁜 일상 속 캠 핑을 못 가더라도 추억할 수 있도록 디자인했다.'
    gr.thumbnail= 'gimage/thum/민경서_캠핑포레스트_썸네일.jpg'
    gr.pic= 'gimage/pic/민경서_캠핑포레스트.jpg'
    gr.picprd= 'gimage/picprd/민경서_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='김인학'
    gr.title= '무어'
    gr.description= '한입에 먹기 좋은 초밥과 야채를 합쳐 만든 음식을 제공하는 브랜드 디자인으로 절제된 패턴 그래픽과 로고를 이용하여 정 적인 브랜드 이미지를 연출하였다.'
    gr.thumbnail= 'gimage/thum/김인학_무어_썸네일.jpg'
    gr.pic= 'gimage/pic/김인학_무어.jpg'
    gr.picprd= 'gimage/picprd/김인학_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='박요한'
    gr.title= '아는 낙곱새'
    gr.description= '모두가 알만큼 맛있다는 의미의 네이밍으로 타이포그래피 스타일의 서체를 이용해 로고를 디자인했다. 전체적으로 모던 한 분위기의 한식당 콘셉트를 브랜딩 했다.'
    gr.thumbnail= 'gimage/thum/박요한_아는 낙곱새_썸네일.jpg'
    gr.pic= 'gimage/pic/박요한_아는 낙곱새.jpg'
    gr.picprd= 'gimage/picprd/박요한_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='강민혁'
    gr.title= '독립만세주'
    gr.description= '‘독립만세주’는 매년 찾아오는 광복절을 기념할 수 있는 전통 증류소주입니다. 순국선열에 대한 감사를 표하고자 국화(國花)인 무궁화와 술 한 잔을 올리자는 뜻에서 제작하였습니다.'
    gr.thumbnail= 'gimage/thum/강민혁_독립만세주_썸네일.jpg'
    gr.pic= 'gimage/pic/강민혁_독립만세주_보드.jpg'
    gr.picprd= 'gimage/picprd/강민혁_연출.jpg'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    for x in gr_list:
        if Work.objects.filter(title=x.title).exists(): #새로고침 시 중복체크
            pass
        else:
            x.save()



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