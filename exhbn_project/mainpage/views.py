from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render (request, 'home.html')

def allprofile(request):
    data_insert()
    allfile = Profile.objects.all()
    ttt = 'Designer'
    return render (request, 'allprofile.html', {'allfile':allfile, 'ttt':ttt})

def detailprofile(request,each_id):
    detail_obj = get_object_or_404(Profile, pk = each_id)
    allwork = Work.objects.all()
    ttt = 'Designer'
    return render (request, 'detailprofile.html', {'ppp':detail_obj, 'works':allwork, 'ttt':ttt})

def about(request):
    ttt = 'About'
    return render (request, 'about.html', {'ttt':ttt})

def worksall(request): #all
    works = Work.objects.all()
    ttt = 'Works'
    return render (request, 'works.html', {'works': works, 'ttt':ttt})

def works(request, wtype): #gd / ad / media
    new_wtype = Type.objects.get(wtype = wtype)
    works = Work.objects.filter(wtype = new_wtype)
    ttt = 'Works'
    return render (request, 'works.html', {'works': works, 't': wtype, 'ttt':ttt})

def work_detail(request, pk): # type1 광고 디자인 ad type2 영상 애니메이션 me type3 그래픽 디자인 gr
    work = Work.objects.filter(pk=pk)
    wtypeObj = Type.objects.get(wtype = work[0].wtype)
    print(wtypeObj)
    wtypeStr = wtypeObj.wtype # ad / me / gr
    print("wtypeStr: "+wtypeStr)
    if wtypeStr == 'ad':
        ttt = 'Advertising Design'
        return render (request, 'work_detail.html', {'work': work, 'ttt':ttt})
    elif wtypeStr == 'me':
        ttt = 'Video Animation'
        return render (request, 'work_detail2.html', {'work': work, 'ttt':ttt})
    elif wtypeStr == 'gr':
        ttt = 'Graphic Design'
        return render (request, 'work_detail3.html', {'work': work,'ttt':ttt})

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
    work_insert_me()
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
    w.description= '돼지저금통에 동전을 채워 저축하듯이 비타민을 내 몸에 채워 저축하라는 의미하는 상품광고이다.'
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

    w = Work()
    w.artist= '김인학'
    w.title= '한눈에 보이는 세상'
    w.description= '외국 운송 업체 기업인 ‘FedEx’의 해외 배송이 매우 빠름을 기업 로고 속 세계지도가 보이는 것으로 표현한 작품이다.'
    w.thumbnail= 'wimage/thum/김인학_한눈에 보이는 세상_썸네일.jpg'
    w.pic= 'wimage/pic/김인학_한눈에 보이는 세상.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김인학'
    w.title= '소리도 먼지도 ZERO'
    w.description= '‘LG전자’의 무선 청소기 코드제로의 상품광고로 악보에 음표를 빨아드리는 모습을 통해 강한 흡입력과 소음이 없음을 표현한 작품이다.'
    w.thumbnail= 'wimage/thum/김인학_소리도 먼지도 ZERO_썸네일.jpg'
    w.pic= 'wimage/pic/김인학_소리도 먼지도 ZERO.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김인학'
    w.title= '불법 다운중'
    w.description= '로딩창과 감옥의 철창을 결합하여 로딩과 동시에 서서히 가둬지는 모습을 통해 불법 다운로드를 하면 누구든지 처벌을 받게 됨을 표현한 작품이다.'
    w.thumbnail= 'wimage/thum/김인학_불법 다운중_썸네일.jpg'
    w.pic= 'wimage/pic/김인학_불법 다운중.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '박요한'
    w.title= '혼자만의 걱정 뚝!'
    w.description= '걱정을 멈추라는 의미의 ‘뚝’과 연필심이 부러지는 소리인 ‘뚝’을 이용해 중의적으로 표현했다. 부러진 연필심과 확성기를 합성해 걱정을 뚝 멈추고 대화로 해결하자는 메시지의 공익광고이다.'
    w.thumbnail= 'wimage/thum/04. 박요한_혼자만의 걱정 뚝_썸네일.jpg'
    w.pic= 'wimage/pic/박요한_혼자만의 걱정 뚝.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '박요한'
    w.title= 'Gatsby Style'
    w.description= '브러쉬의 솔 부분을 왁스로 스타일링한 헤어처럼 표현하여 개성있는 스타일들을 연출했다. 갸스비의 스타일링 왁스를 홍보하는 상품광고이다.'
    w.thumbnail= 'wimage/thum/04. 박요한_GatsbyStyle_썸네일.jpg'
    w.pic= 'wimage/pic/박요한_GatsbyStyle.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '박요한'
    w.title= '밝히지 마세요!'
    w.description= '불법촬영문제의 대한 공익광고로, 손전등과 카메라 렌즈를 합성하여 이성을 밝히지 말라는 중의적 의미를 표현하였다.'
    w.thumbnail= 'wimage/thum/04. 박요한_밝히지 마세요!_썸네일.jpg'
    w.pic= 'wimage/pic/박요한_밝히지 마세요!.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '강민혁'
    w.title= '태아의 소리'
    w.description= '본 작품은 귀와 태아의 형태를 절묘하게 결합한 이미지를 통해 메시지를 전달하고자 했다. 마치 태아가 귀에 대고 부모님을 향해 속삭이는 듯한 메시지는 낙태에 대한 많은 의미를 함축적으로 나타내고 있다.'
    w.thumbnail= 'wimage/thum/강민혁_태아의소리_썸네일.jpg'
    w.pic= 'wimage/pic/강민혁_태아의 소리_웹.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '강민혁'
    w.title= '한국의 미'
    w.description= '본 작품은 ‘아모레 퍼시픽’의 기업이념을 담은 광고 포스터이다. 동양적인 느낌의 아름다울 ‘美’자를 마스카라로 힘차게 내리친 느낌을 통해 한국과 동양을 대표하여 뷰티사업군을 이끌겠다는 포부를 표현했다.'
    w.thumbnail= 'wimage/thum/강민혁_한국의미_썸네일.jpg'
    w.pic= 'wimage/pic/강민혁_한국의 미_웹.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '강민혁'
    w.title= 'Sweet Champion'
    w.description= 'FIFA 월드컵 트로피와 ‘페레로로쉐’의 형태적 유사성을 결합한 상품광고이다. 트로피가 주는 ‘챔피온’의 의미와 ‘페레로로쉐’가 주는 ‘초콜릿’이라는 의미를 합쳐 메시지를 전달하고자 했다.'
    w.thumbnail= 'wimage/thum/강민혁_sweet dream_썸네일.jpg'
    w.pic= 'wimage/pic/강민혁_Sweet dream_웹.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '류호경'
    w.title= '인생은 다시 U-turn 할 수 없습니다.'
    w.description= '음주운전에 위험성과 음주운전으로 생을 마감하여 한 순간의 실수로 인생이 다시 돌아 올 수 없다는 것을 보여주는 공익광고 디자인을 하였다.'
    w.thumbnail= 'wimage/thum/류호경_썸네일(1).jpg'
    w.pic= 'wimage/pic/류호경_인생은 다시 U-turn할 수 없습니다..jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '정명현'
    w.title= '가장 쉬운 이웃 사랑법'
    w.description= '포개어진 빨간 슬리퍼와 하트 모양의 형태적 유사성을 이용해 이웃 간의 새로운 사랑법을 표현한 층간 소음 공익광고이다.'
    w.thumbnail= 'wimage/thum/정명현_가장 쉬운 이웃 사랑법_썸네일.jpg'
    w.pic= 'wimage/pic/정명현_가장 쉬운 이웃 사랑법.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '정명현'
    w.title= '깨끗한 옷으로 되감기'
    w.description= '미디어 플레이어의 되감기 버튼의 형태와 깔끔한 셔츠 옷깃의 형태적 유사성을 이용해 제작한 ‘크린토피아’ 기업광고이다.'
    w.thumbnail= 'wimage/thum/정명현_깨끗한 옷으로 되감기_썸네일.jpg'
    w.pic= 'wimage/pic/정명현_깨끗한 옷으로 되감기.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '정명현'
    w.title= '얼룩, 치료!'
    w.description= '주사기 속 하단으로 내려갈수록 점점 더러워지는 빨래들을 배치해 얼룩을 치료한다는 메시지를 표현한 ‘크린토피아’ 기업광고이다.'
    w.thumbnail= 'wimage/thum/정명현_얼룩,치료!_썸네일.jpg'
    w.pic= 'wimage/pic/정명현_얼룩,치료!.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '정명현'
    w.title= '한국인의 힘'
    w.description= '한국 전통 관악기와 상품의 형태적 특징을 이용해 홍삼의 100년 전통을 표현한 ‘홍삼정 애브리 타임’ 상품광고이다.'
    w.thumbnail= 'wimage/thum/정명현_한국인의 힘_썸네일.jpg'
    w.pic= 'wimage/pic/정명현_한국인의 힘.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '박효정'
    w.title= '물 방전'
    w.description= '이 작품은 물을 절약하자는 공익광고 포스터다. 페트병에 소량의 물이 담긴 모습과 배터리가 방전된 모습을 결합하여 우리나라는 물 부족 국가라는 심각성을 나타내었다.'
    w.thumbnail= 'wimage/thum/박효정_물 방전_썸네일.jpg'
    w.pic= 'wimage/pic/박효정_물 방전.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '박효정'
    w.title= '숨 막히는 자연, 목 막히는 자연'
    w.description= '이 작품은 일회용품 사용을 줄이자는 공익광고 포스터다. 종이컵을 코끼리의 코와 기린의 목과 결합하여 무분별하게 사용되는 일회용품의 심각성을 나타내었다.'
    w.thumbnail= 'wimage/thum/박효정_숨 막히는 자연, 목 막히는 자연_썸네일.jpg'
    w.pic= 'wimage/pic/박효정_숨 막히는 자연, 목 막히는 자연.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '박효정'
    w.title= '무풍에어컨'
    w.description= '이 작품은 ‘삼성 무풍 에어컨’을 홍보하는 광고 포스터다. 민들레 홀씨가 바람에 날리지 않고 그대로 얼어버린 모습으로 무풍 에어컨의 장점을 극대화하여 표현하였다.'
    w.thumbnail= 'wimage/thum/박효정_무풍에어컨_썸네일.jpg'
    w.pic= 'wimage/pic/박효정_무풍에어컨.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '박주이'
    w.title= '담배 때려치워!'
    w.description= '담배와 샌드백을 합쳐 ‘담배를 때려치우다’와 ‘샌드백을 때리다’라는 언어유희와 담배를 그만하자는 의미의 금연 공익광고이다.'
    w.thumbnail= 'wimage/thum/박주이_담배 때려치워!_썸네일.jpg'
    w.pic= 'wimage/pic/박주이_담배 때려치워!.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '신혜현'
    w.title= '찐한 커피향'
    w.description= '턴테이블에 비유하여 진한 원두의 커피 향을 느낄 수 있음을 표현한 광고이다.'
    w.thumbnail= 'wimage/thum/신혜현_찐한 커피향_썸네일.jpg'
    w.pic= 'wimage/pic/신혜현_찐한 커피향.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '오동우'
    w.title= '사랑, 행복의 CJ'
    w.description= '‘CJ그룹’ 기업 로고를 각각 사랑의 열매, 세잎클로버의 형태와 결합하여 소비자에게 사랑과 행복을 드린다는 기업광고이다.'
    w.thumbnail= 'wimage/thum/오동우_CJ_썸네일.jpg'
    w.pic= 'wimage/pic/오동우_CJ.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '오동우'
    w.title= '보호막이 펼쳐진다'
    w.description= '아큐브 렌즈의 24시간 동안 지속되는 촉촉함과 아큐브의 안정성을 우산에 비유하여 아큐브 렌즈 상품광고를 제작했다.'
    w.thumbnail= 'wimage/thum/오동우_아큐브_썸네일.jpg'
    w.pic= 'wimage/pic/오동우_아큐브.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '오동우'
    w.title= '방심하면 터집니다'
    w.description= 'COVID-19바이러스를 풍선과 결합하여 풍선이 쉽게 터지는 것처럼 COVID-19바이러스도 방심하면 다시 심각해진다는 컨셉의 공익광고이다.'
    w.thumbnail= 'wimage/thum/오동우_코로나_썸네일.jpg'
    w.pic= 'wimage/pic/오동우_코로나.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '신진경'
    w.title= '델몬트 바나나'
    w.description= '델몬트 바나나와 글러브의 유사함을 결합시킨 작품이다. Nice Catch!라는 헤드라인을 통해 달콤한 과일의 맛을 잡았다는 것을 표현하였다.'
    w.thumbnail= 'wimage/thum/신진경_델몬트바나나_썸네일.jpg'
    w.pic= 'wimage/pic/신진경_델몬트바나나.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김민서'
    w.title= 'There’s no time'
    w.description= '해수면 위의 빙하 조각을 심박동으로 표현해 북극의 시간이 얼마 남지 않았음을 경고하는 ‘GREENPEACE’ 공익광고이다.'
    w.thumbnail= 'wimage/thum/김민서_There_s no time_썸네일.jpg'
    w.pic= 'wimage/pic/김민서_There_s no time.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김민서'
    w.title= 'enjoy playing'
    w.description= '‘Durex’ 콘돔과 고리 던지기 게임을 결합하여 콘돔으로 안전하고 성생활을 즐기라는 메시지를 전달하고자 했다.'
    w.thumbnail= 'wimage/thum/김민서_enjoy playing~_썸네일.jpg'
    w.pic= 'wimage/pic/김민서_enjoy playing.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김민서'
    w.title= '신발의 기준을 새로 쓰다'
    w.description= '‘슈펜’을 3색 볼펜에 빗대어 합리적으로 신발의 기준을 새로 쓰는 브랜드임을 알리는 기업광고이다.'
    w.thumbnail= 'wimage/thum/김민서_신발의 기준을 새 로 쓰다_썸네일.jpg'
    w.pic= 'wimage/pic/김민서_신발의 기준을 새로 쓰다.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김예지'
    w.title= 'WATER POWER!'
    w.description= '‘니베아’ 립밤의 수분감을 분사기로 표현한 상품광고이다. 배경에 물방울들을 넣어 수분감을 더 극대화 시켜보려 하였고 립밤과 분사기 부분은 3D로 구현하여 표현하였다.'
    w.thumbnail= 'wimage/thum/김예지_썸네일.jpg'
    w.pic= 'wimage/pic/김예지_ WATER POWER!.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '전예린'
    w.title= '음주V운전'
    w.description= '맞춤법 표기와 타이포를 이용한 음주운전 공익광고이다. 함께해서는 안되는 음주와 운전은 띄어쓰기 표기법을 이용해 표현하였다.'
    w.thumbnail= 'wimage/thum/전예린_음주V운전_썸네일.jpg'
    w.pic= 'wimage/pic/전예린_음주V운전.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '전예린'
    w.title= '매콤함이 펑!'
    w.description= '‘타바스코’ 소스의 강력한 매콤함을 수류탄을 이용해 표현한 상품광고이다. 피어오르는 수류탄 연기가 얼얼한 매운맛을 더 강조해준다.'
    w.thumbnail= 'wimage/thum/전예린_매콤함이 펑!_썸네일.jpg'
    w.pic= 'wimage/pic/전예린_매콤함이 펑!.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '전예린'
    w.title= '화끈한 한방울!'
    w.description= '흘러내리는 ‘타바스코’ 소스의 매운맛을 고추로 비유해 표현한 광고다. 소스 병에서 흘러내리는 한 방울을 매콤한 고추에 비유한 상품광고이다. ‘타바스코’ 소스의 화끈한 매운맛을 강조해보았다.'
    w.thumbnail= 'wimage/thum/전예린_화끈한 한 방울!_썸네일.jpg'
    w.pic= 'wimage/pic/전예린_화끈한 한 방울!.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '전예린'
    w.title= '인생에 범죄를 쓰다'
    w.description= '포승줄에 묶인 만년필의 촉을 손을 이용해 경각심을 주는 저작권 보호에 대한 공익광고이다. 저작권 침해로 본인 인생에 범죄를 쓰게 된다는 의미를 함께 담았다.'
    w.thumbnail= 'wimage/thum/전예린_인생에 범죄를 쓰다_썸네일.jpg'
    w.pic= 'wimage/pic/전예린_인생에 범죄를 쓰다.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김나영'
    w.title= '안전전기벨트'
    w.description= '안전한 전기 사용법은 우리들의 생명과 재산을 보호해 주는 행위이고 전기재해로부터 우리들의 안전을 책임지는 ‘전기안전 지킴이’로서 안심하고 사용할 수 있도록 지키자는 광고 포스터이다.'
    w.thumbnail= 'wimage/thum/김나영_안전전기벨트_썸네일.jpg'
    w.pic= 'wimage/pic/김나영_안전전기벨트.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김나영'
    w.title= '꽉! 잠그세요!'
    w.description= '‘한국전기안전공사’는 전기재해로부터 우리들의 안전을 책임지는 ‘전기안전 지킴이’로서 안심하고 사용할 수 있으며 사소한 행동으로 전기에너지 안전의식을 지키자는 광고 포스터이다.'
    w.thumbnail= 'wimage/thum/김나영_꽉! 잠그세요!_썸네일.jpg'
    w.pic= 'wimage/pic/김나영_꽉! 잠그세요!.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '김영경'
    w.title= '오늘 하루 충전완료, 하루의 시작'
    w.description= '이 작품은 ‘탐앤탐스’ 기업광고 포스터다. 커피를 먹음으로써 하루를 충전하고, 시작한다는 것을 표현한 작품이다.'
    w.thumbnail= 'wimage/thum/김영경_오늘 하루 충전완료!, 하루의 시작_썸네일.jpg'
    w.pic= 'wimage/pic/김영경_오늘 하루 충전 완료!, 하루의 시작.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '안예은'
    w.title= '지식을 열다'
    w.description= '독서를 통해 지식을 얻는 모습을 마치 어둠 속의 지퍼가 열리면서 빛이 들어오는 것처럼 표현한 광고디자인이다.'
    w.thumbnail= 'wimage/thum/안예은_지식을 열다_썸네일.jpg'
    w.pic= 'wimage/pic/안예은_지식을 열다.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '지광민'
    w.title= '불법다운로드'
    w.description= '이 작품은 불법 다운로드를 해선 안된다는 공익광고 포스터다. USB메모리를 생선회처럼 집는 것으로 누군가의 아이디어나 자료를 날로 먹는다는 것으로 표현했다.'
    w.thumbnail= 'wimage/thum/지광민_날로 먹겠습니까__썸네일.jpg'
    w.pic= 'wimage/pic/지광민_날로 먹겠습니까_.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '한승희'
    w.title= 'Star lignt helneken'
    w.description= '‘하이네켄’과 별자리를 결합하며 반짝이는 ‘하이네켄’과 함께 밤하늘의 즐거움을 경험해 보라는 의미를 담고 있는 기업광고이다.'
    w.thumbnail= 'wimage/thum/한승희_Star lignt helneken_썸네일.jpg'
    w.pic= 'wimage/pic/한승희_Star lignt helneken.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '한승희'
    w.title= '전기 돋보기'
    w.description= '돋보기와 원형 전구를 결합하여 주변에 쓰지 않은 콘센트가 있는지 없는지 돋보기 보듯 꼼꼼히 살펴보자는 의미를 담아 진행한 에너지 절약 공익광고이다.'
    w.thumbnail= 'wimage/thum/한승희_전기 돋보기_썸네일.jpg'
    w.pic= 'wimage/pic/한승희_전기 돋보기.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '한승희'
    w.title= '에너지 절약 경고'
    w.description= '경고 카드와 콘센트를 결합하여, 에너지를 절약하지 않는 사람에게 경고의 카드를 내밀어 주변에 쓰지 않는 코드가 꽂혀있지 않은지 다시 한 번 살펴보라는 컨셉을 가지고 진행한 에너지 절약 공익광고이다.'
    w.thumbnail= 'wimage/thum/한승희_에너지 절약 경고_썸네일.jpg'
    w.pic= 'wimage/pic/한승희_에너지 절약 경고.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '홍성현'
    w.title= '바셀린'
    w.description= '피부 보습제 ‘바셀린’의 성능을 홍보하는 목적으로 제작된 광고 디자인이며, 상품에 포인트로 들어간 블루 컬러를 메인으로 ‘바셀린’의 촉촉함과 보습력을 강조하여 나타내었다.'
    w.thumbnail= 'wimage/thum/홍성현_바셀린_썸네일.jpg'
    w.pic= 'wimage/pic/홍성현_바셀린.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '홍성현'
    w.title= '네이버'
    w.description= '포털사이트로 더 잘 알려진 기업 ‘네이버’의 다양한 서비스들을 홍보하는 목적으로 디자인 한 작품으로, ‘다양함’이라는 키워드를 여러 가지 색상들이 모여 있는 컬러 차트에 비유하여 나타낸 광고 작품이다.'
    w.thumbnail= 'wimage/thum/홍성현_네이버_썸네일.jpg'
    w.pic= 'wimage/pic/홍성현_네이버.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '홍성현'
    w.title= '한국자산관리공사'
    w.description= '‘한국자산관리공사’ 기업을 홍보하는 목적으로 디자인 한 광고 작품으로, 통조림 캔의 오래가는 특징을 역 이용하여 오랫동안 방치되고 관리되지 못해왔던 자산을 한국 자산 관리공사에서 관리해 준다는 의미이다.'
    w.thumbnail= 'wimage/thum/홍성현_한국자산관리공사_썸네일.jpg'
    w.pic= 'wimage/pic/홍성현_한국자산관리공사.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '장함'
    w.title= '소음경고'
    w.description= '마이크와 경보등을 결합해 소음의 오염을 줄여야 한다고 경고한다.'
    w.thumbnail= 'wimage/thum/장함_ 썸네일.jpg'
    w.pic= 'wimage/pic/장함_ 소음 경고.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '장함'
    w.title= '우유의 힘!'
    w.description= '팔 근육으로 표현하면 ‘서울우유’는 영양가가 높고 다 마시면 힘이 많이 난다는 것을 표현한 작품이다.'
    w.thumbnail= 'wimage/thum/장함_썸네일.jpg'
    w.pic= 'wimage/pic/장함_ 우유의 힘.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '우삼청'
    w.title= 'KUMHO TIRE 타이어'
    w.description= '에어캡으로 타이어 표면의 무늬를 볼록하게 교체해 ‘금호타이어’가 안전하고 편하다는 특징을 표현하였다.'
    w.thumbnail= 'wimage/thum/우삼청_KUMHO TIRE 타이어_썸네일.jpg'
    w.pic= 'wimage/pic/우삼청_KUMHO TIRE 타이어.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '우삼청'
    w.title= '안전벨트를 착용한 운전'
    w.description= '안전벨트와 칼을 결합하여 운전 중 안전벨트를 풀면 위험하다는 것을 표현했다.'
    w.thumbnail= 'wimage/thum/우삼청_안전벨트를 착용한 운전_썸네일.jpg'
    w.pic= 'wimage/pic/우삼청_안전벨트를 착용한 운전.jpg'
    w.wtype=Type.objects.get(wtype = 'ad')
    work_list.append(w)

    w = Work()
    w.artist= '임운유'
    w.title= '금연 광고'
    w.description= '다 타버린 담배로 병상에 있는 환자를 표현하고, 담배를 피우면 목숨이 담배처럼 사라진다는 사실을 알려주는 금연 공익광고이다.'
    w.thumbnail= 'wimage/thum/임운유_금연 광고 1_썸네일.jpg'
    w.pic= 'wimage/pic/임운유_금연 광고 1.jpg'
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
    gr.description= '무분별한 분양과 무책임한 방치, 유기 때문에 고통을 받는 반려동물들이 많아지고 있다. 그러한 상황을 타파하기 위해서 반려 동물 등록제와 연동 가능한 애플리케이션을 디자인하였다.'
    gr.thumbnail= 'gimage/thum/김선식_P_P_썸네일.jpg'
    gr.pic= 'gimage/pic/김선식_P_P.jpg'
    gr.picprd= 'gimage/picprd/김선식_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='민경서'
    gr.title= '캠핑 포레스트'
    gr.description= '캠핑은 계절과 관계없이 언제든 즐길 수 있는 활동이라는 것을 표현하고 계절별로 캠핑을 했을 때 느낄 수 있는 매력을 보 여주려 했다. 계절뿐만 아니라 밤과 낮, 새벽 시간에 따라 다른 매력과 활동들을 소개했다. 일러스트를 보며 바쁜 일상 속 캠핑을 못 가더라도 추억할 수 있도록 디자인했다.'
    gr.thumbnail= 'gimage/thum/민경서_캠핑포레스트_썸네일.jpg'
    gr.pic= 'gimage/pic/민경서_캠핑포레스트.jpg'
    gr.picprd= 'gimage/picprd/민경서_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='김인학'
    gr.title= '무어'
    gr.description= '한입에 먹기 좋은 초밥과 야채를 합쳐 만든 음식을 제공하는 브랜드 디자인으로 절제된 패턴 그래픽과 로고를 이용하여 정적인 브랜드 이미지를 연출하였다.'
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
    gr.picprd= 'gimage/picprd/강민혁_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='류호경'
    gr.title= '예스럽다'
    gr.description= '한복은 삼국시대부터 입기 시작했고, 중국의 주장은 한복이 명나라로부터 왔다고 하지만 삼국시대 때는 명나라는 존재하지 않았다. 양직공도나 고구려 고분을 보면 알 수 있듯 한복은 고대한국으로부터 내려온 전통의상이라고 할 수 있다. 한복이 우리나라 전통의상이라는 것을 알리기 위해서 장신구와 전통패턴으로 포스터디자인 캘린더를 제작했다.'
    gr.thumbnail= 'gimage/thum/류호경_썸네일.jpg'
    gr.pic= 'gimage/pic/류호경_예스럽다.jpg'
    gr.picprd= 'gimage/picprd/류호경_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='정명현'
    gr.title= '오복밥집'
    gr.description= '혼자 사는 사람들이 언제든지 편하게 들러서 맛있고 건강한 집 밥 같은 음식을 즐길 수 있는, 깔끔하고 편안한 분위기의 한 식당이다. 바쁜 학생이나 직장인들을 위한 배달, 포장 서비스도 개발했다.'
    gr.thumbnail= 'gimage/thum/정명현_썸네일.jpg'
    gr.pic= 'gimage/pic/정명현_오복밥집.jpg'
    gr.picprd= 'gimage/picprd/정명현_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='박효정'
    gr.title= 'HOME SWEET HOME'
    gr.description= '여행을 떠나지 못해 집에서라도 랜선 여행의 느낌을 줄 수 있도록 랜드마크와 ‘아이키’라는 댄서의 캐릭터를 담은 캘린더 디자인이다. 높은 채도의 7가지 컬러를 활용하여 활발하고 생기 있는 느낌을 주었다.'
    gr.thumbnail= 'gimage/thum/박효정_썸네일.jpg'
    gr.pic= 'gimage/pic/박효정_HOME SWEET HOME.jpg'
    gr.picprd= 'gimage/picprd/박효정_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='박주이'
    gr.title= ' I’M O'
    gr.description= '친환경 생리대 브랜드 ‘I’M O’는 여성의 건강과 안전을 최우선으로 생각하며 원료부터 생산과정까지 따져 고객을 만족시키는 것이 목표인 브랜드이다. I’M O의 상징인 무당벌레를 이용하여 브랜드 로고를 리디자인했으며 여성의 유동적인 모습을 그린 일러스트로 패키지, 캘린더, 굿즈를 디자인했다.'
    gr.thumbnail= 'gimage/thum/박주이_썸네일.jpg'
    gr.pic= 'gimage/pic/박주이_아임오 로고 리디자인.jpg'
    gr.picprd= 'gimage/picprd/박주이_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='원도윤'
    gr.title= '장승이네'
    gr.description= '충남 공주시의 장승마을을 주제로 제작한 패턴 디자인이다. 어린이들을 대상으로 인디언 장승을 단순화하고 다채로운 컬러를 사용했다. 장승이네는 장승이, 장군이, 장돌이 세 캐릭터로 각각 어울리는 인디언 문양을 조합하여 패턴을 디자인했다.'
    gr.thumbnail= 'gimage/thum/원도윤_썸네일.jpg'
    gr.pic= 'gimage/pic/원도윤_장승이네.jpg'
    gr.picprd= 'gimage/picprd/원도윤_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='신혜현'
    gr.title= '파라다이스'
    gr.description= '파라다이스는 일에 치여 사는 현대인에게 맥주 한 잔으로 잠시나마 바다를 다녀온 듯한 느낌을 선사하는 맥주 브랜드이다. 바다를 상징하는 고래, 돛단배, 파도를 모티브로 한 캐릭터를 제작하여 브랜드 아이덴티티를 구축하고자 했다.'
    gr.thumbnail= 'gimage/thum/신혜현_썸네일.jpg'
    gr.pic= 'gimage/pic/신혜현_파라다이스.jpg'
    gr.picprd= 'gimage/picprd/신혜현_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='오동우'
    gr.title= 'The higher'
    gr.description= '도쿄 올림픽에서 우리에게 큰 감동을 준 선수들과 올림픽 상징 구호인 ‘더 높게’ 문구를 선정하여 우리에게 큰 감동과 더 높은 곳으로 성장할 수 있다는 콘셉트로 한 달력 디자인이다.'
    gr.thumbnail= 'gimage/thum/오동우_The higher_썸네일.jpg'
    gr.pic= 'gimage/pic/오동우_The higher.jpg'
    gr.picprd= 'gimage/picprd/오동우_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='최영현, 최현우'
    gr.title= 'Overandus'
    gr.description= '인터넷 사업을 하는 의류업체의 자신의 스타일을 구상할 수 있는 앱이며, 나만의 스타일을 누군가에게 보여줄 수 있다. 또한 공유가 가능하기 때문에 인플루언서가 될 기회를 얻을 수 있는 UI/UX 디자인 작품이다.'
    gr.thumbnail= 'gimage/thum/최영현최현우_오버앤어스_썸네일.png'
    gr.pic= 'gimage/pic/최영현, 최현우_오버앤어스.jpg'
    gr.picprd= 'gimage/picprd/최영현, 최현우_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='신진경'
    gr.title= '말티숑 이브'
    gr.description= '말티즈와 비숑의 유전자가 섞인 강아지 이브를 캐릭터화해서 만든 작품으로 이브의 일상을 표현하였다. 말티즈를 닮았지만 곱슬거리는 털이 포인트인 이브의 장난스러운 모습을 담아낸 작품이다.'
    gr.thumbnail= 'gimage/thum/신진경_말티숑이브_썸네일.jpg'
    gr.pic= 'gimage/pic/신진경_말티숑이브.jpg'
    gr.picprd= 'gimage/picprd/신진경_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='김민서'
    gr.title= 'TOYFUL'
    gr.description= 'TOYFUL은 ‘기쁨을 주는’ 이라는 뜻을 가진 JOYFUL과 유사한 발음을 가진 것에서 착안한 타이틀로써 저소득 아동에게 장난감을 통해 기쁨을 선물하겠다는 뜻을 담은 토이저러스 캠페인 디자인이다.'
    gr.thumbnail= 'gimage/thum/김민서_썸네일.jpg'
    gr.pic= 'gimage/pic/김민서_TOYFUL.jpg'
    gr.picprd= 'gimage/picprd/김민서_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='김예지'
    gr.title= '다온'
    gr.description= '평소 잘 사용하지 않지만 우리나라의 전통이 담겨있는 노리개를 이용하여 가상의 브랜드를 직접 만들어 패턴이나 일러스트화 시켜 표현한 패키지 디자인이다.'
    gr.thumbnail= 'gimage/thum/김예지_썸네일.jpg'
    gr.pic= 'gimage/pic/김예지_다온.jpg'
    gr.picprd= 'gimage/picprd/김예지_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='전예린'
    gr.title= '우리의 것'
    gr.description= '수백 년의 역사가 살아 숨 쉬는 우리나라 전통문화. 오랜 세월을 굳건히 함께한 만큼, 서로 다른 보물들과 이야기를 품고 있다. 어렵게 다가올 수 있지만 친근하고 정겨운 캐릭터로 가까워지는 시간을 갖고 싶다.'
    gr.thumbnail= 'gimage/thum/전예린_썸네일.jpg'
    gr.pic= 'gimage/pic/전예린_우리의 것!.jpg'
    gr.picprd= 'gimage/picprd/전예린_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='김나영'
    gr.title= '안다미로'
    gr.description= '‘안다미로’는 ‘담은 것이 그릇에 넘치도록 많게’라는 뜻으로 청풍면 도곡리의 많은 볼거리와 체험할 곳, 좋은 황토에서 나오는 농산물이 가득한 마을을 지칭하는 브랜드명이다.'
    gr.thumbnail= 'gimage/thum/김나영_썸네일.jpg'
    gr.pic= 'gimage/pic/김나영_안다미로.jpg'
    gr.picprd= 'gimage/picprd/김나영_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='김다은'
    gr.title= '필코'
    gr.description= '‘필코’는 친환경 활동을 재미있게 참여할 수 있도록 도와주는 소셜 앱 서비스이다. 필환경 활동의 저조한 실천률을 높이고자 실시간 인증 형식의 도전과제들로 동기부여와 참여의식을 높여준다. 필코는 작은 실천들이 모여 위대한 변화를 이룬다는 슬로건처럼 친환경 생활습관 형성에 도움을 주는 것이 목표이다.'
    gr.thumbnail= 'gimage/thum/김다은_썸네일.jpg'
    gr.pic= 'gimage/pic/김다은_2020캘린더.jpg'
    gr.picprd= 'gimage/picprd/김다은_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='김영경'
    gr.title= '여행이 고프다'
    gr.description= '2021년 코로나 바이러스로 인해 여행을 계획했던 많은 사람들이 모든 계획을 취소하고 여행을 나중으로 밀었다. 여행을 가지 못하게 된 아쉬운 마음을 달래고자 가고 싶은 나라들을 일러스트로 표현하여 캘린더들 디자인했다.'
    gr.thumbnail= 'gimage/thum/김영경_썸네일.jpg'
    gr.pic= 'gimage/pic/김영경_여행이고프다.jpg'
    gr.picprd= 'gimage/picprd/김영경_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='안예은'
    gr.title= '후드덕'
    gr.description= '‘후드덕’은 오리를 모티브로 한 캐릭터로 모두가 친근하게 받아들일 수 있도록 심플하고 귀엽게 디자인하였다. 옐로우 컬러를 메인으로 사용해서 포근하며 발랄한 이미지를 주도록 하였다.'
    gr.thumbnail= 'gimage/thum/안예은_썸네일.jpg'
    gr.pic= 'gimage/pic/안예은_후드덕.jpg'
    gr.picprd= 'gimage/picprd/안예은_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='정예림'
    gr.title= 'People cloz'
    gr.description= '패션을 좋아하는 누구나 패션 정보를 공유하며 색다른 패션 트렌드를 만들어나가는 공간. AR 카메라, 착장 스케치를 통해 쇼핑도 재밌고 윤택하게 할 수 있는 앱이다. AR 카메라를 통해 옷을 미리 코디해 볼 수 있으며 착장 스케치를 통해 쇼핑하고자 하는 옷을 코디해 볼 수 있다는 부분이 이 애플리케이션에서 가장 강점인 기능이다.'
    gr.thumbnail= 'gimage/thum/정예림_썸네일.jpg'
    gr.pic= 'gimage/pic/정예림_people clo z.jpg'
    gr.picprd= 'gimage/picprd/정예림_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='지광민'
    gr.title= '2022 범돌이의 일 년'
    gr.description= '2022년 호랑이의 해를 맞이해 호랑이 캐릭터 범돌이가 날짜에 맞춰 1년 동안의 사계절을 만끽하며 알차게 살아가는 모습을 보여주는 캘린더 디자인이다.'
    gr.thumbnail= 'gimage/thum/지광민_2022 범돌이의 일년_썸네일.jpg'
    gr.pic= 'gimage/pic/지광민_2022 범돌이의 일년.jpg'
    gr.picprd= 'gimage/picprd/지광민__연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='한승희'
    gr.title= 'Zdian sign'
    gr.description= '밤하늘을 빛내는 별자리를 알리기 위한 인포그래픽을 제작했다. 누구나 쉽게 볼수 있게 일러스트 위주로 제작했으며, 12황도라 불리는 별자리에는 색을 넣어 그 외의 별자리와 다르게 차별성을 두었다.'
    gr.thumbnail= 'gimage/thum/한승희_썸네일.jpg'
    gr.pic= 'gimage/pic/한승희_zodiac sign.jpg'
    gr.picprd= 'gimage/picprd/한승희_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='홍성현'
    gr.title= '멜린 초콜릿'
    gr.description= '달달한 특제 과일 시럽이 특징인 프리미엄 초콜릿 브랜드 ‘Mellin’을 브랜딩한 디자인 작품이다. 대중적이지 않은 과일들에서 오는 특별한 맛과 친숙한 과일들을 진하게 녹여 낸 시럽처럼 패키지 역시 각각의 과일 모양 속에 통통 튀는 패턴들이 담겨 있다.'
    gr.thumbnail= 'gimage/thum/홍성현_썸네일.jpg'
    gr.pic= 'gimage/pic/홍성현_멜린초콜릿.jpg'
    gr.picprd= 'gimage/picprd/홍성현_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='나우팔'
    gr.title= 'COLASIA'
    gr.description= '말레이시아는 이슬람교의 문화를 따라 대부분이 히잡으로 스카프를 착용한다. 말레이시아, 중국, 인도 세 개의 주요 인종이 있고 종족마다의 고유의 전통에 따른 히잡 패턴을 제작하였다.'
    gr.thumbnail= 'gimage/thum/나우팔_썸네일.jpg'
    gr.pic= 'gimage/pic/나우팔_COLASIA.jpg'
    gr.picprd= 'gimage/picprd/나우팔_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='장함'
    gr.title= '청화자'
    gr.description= '청화자는 중국 도자기의 주류 품종 중 하나로 무늬가 매우 섬세하고 독특하기 때문에 색채가 단일하지만 변화무쌍하며 현대 유행하는 중국 문화 원소이다. 작품과 전통문화 요소를 특색있는 지역문화를 담은 우표디자인 작품을 제작하였다.'
    gr.thumbnail= 'gimage/thum/장함_썸네일.jpg'
    gr.pic= 'gimage/pic/장함_ 청화자.jpg'
    gr.picprd= 'gimage/picprd/장함  _연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='고벽영'
    gr.title= '나의 즐거운 삶'
    gr.description= '삶을 주제로 만든 우표로 좋아하는 음식(케이크,콜라,우유 등)과 삶의 일부 모습을 담아 제작한 캐릭터 디자인이다. 색상은 산뜻하고 심플한 컬러로 구성했다.'
    gr.thumbnail= 'gimage/thum/고벽영_썸네일.jpg'
    gr.pic= 'gimage/pic/고벽영_나의 즐거운 삶.jpg'
    gr.picprd= 'gimage/picprd/고벽영_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='우삼청'
    gr.title= '중국의 명경치'
    gr.description= '중국의 유명한 풍경인 계린산수, 대만 일월담, 안후이 황산, 베경 고궁, 항저우시후, 쑤저우 원림, 창장 산협, 만리장성의 우표 디자인이다. 중국의 대표적인 풍경들을 골라 우표를 제작하였다.'
    gr.thumbnail= 'gimage/thum/우삼청_썸네일.jpg'
    gr.pic= 'gimage/pic/우삼청_중극의 명경치.jpg'
    gr.picprd= 'gimage/picprd/우삼청_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)

    gr = Work()
    gr.artist='임운유'
    gr.title= '경극'
    gr.description= '중국 전통 경극은 세계 각지를 돌아다니며 중국 전통예술 문화를 소개하고 전파하는 중요한 매개체이다. 이 경극을 모티브로 중국적 특색을 살리고 경극적 요소를 가미한 우표 디자인이다.'
    gr.thumbnail= 'gimage/thum/임운유_썸네일.jpg'
    gr.pic= 'gimage/pic/임운유_경극우표.jpg'
    gr.picprd= 'gimage/picprd/임운유_연출.png'
    gr.wtype=Type.objects.get(wtype = 'gr')
    gr_list.append(gr)


    for x in gr_list:
        if Work.objects.filter(title=x.title).exists(): #새로고침 시 중복체크
            pass
        else:
            x.save()

def work_insert_me():
    media_list = []

    me = Work()
    me.artist= '민경서, 박효정'
    me.title= '시선을 바꾸면 세상이 보인다'
    me.description= '세계 여러 나라의 중소기업에 대한 인식 차이를 보여주고, 중소기업의 사회적 역할과 가치를 바로 알리기 위한 영상이다. 개성있는 캐릭터와 보라색 계열의 메인 컬러, 노란색의 포인트 컬러를 사용하여 모션그래픽으로 표현했다.'
    me.thumbnail= 'mimage/thum/민경서,박효정_썸네일.jpg'
    me.pic= 'mimage/pic/민경서,박효정_시선을 바꾸면 세상이 보인다.jpg'
    me.youtube= 'https://www.youtube.com/embed/Q5OL_ghmJv0'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '민경서'
    me.title= '낙서'
    me.description= '서로의 감정이 무뎌져 마치 종잇장위의 낙서처럼 얼룩져가고 흐려지는 연인에 대한 상실감을 낙서를 통해 풀어낸 노래로 가사에 맞는 라인드로잉을 모션그래픽으로 제작하였다. 베이지와 블루, 회색을 사용하여 식은 연인들의 마음을 표현했다.'
    me.thumbnail= 'mimage/thum/민경서_썸네일.jpg'
    me.pic= 'mimage/pic/민경서_낙서.jpg'
    me.youtube= 'https://www.youtube.com/embed/7Y-Anvjk6VY'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '강민혁, 정명현'
    me.title= '아버지'
    me.description= '본 영상은 KB 국민은행의 애니메이션 광고이다. 아버지와 그를 그리워하는 아들의 스토리를 담았고, 아버지를 그림자로 표현해 가는 길을 함께 걸어가고 있다는 것으로 모든 아버지의 희생과 든든함을 보여주는 작품이다.'
    me.thumbnail= 'mimage/thum/강민혁,정명현_썸네일.jpg'
    me.pic= 'mimage/pic/강민혁, 정명현_아버지.jpg'
    me.youtube= 'https://www.youtube.com/embed/yZhY6qRzfpE'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '강민혁, 정명현'
    me.title= '중소기업, 다시 바라보기'
    me.description= '본 영상은 중소기업 인식 개선을 위한 인포그래픽 영상이다. 99.83%라는 국내 중소기업의 막대한 비율을 소개하는 것을 시작으로 중소기업만의 혜택, 장점들을 다양한 애니메이션 함께 담아내었다.'
    me.thumbnail= 'mimage/thum/강민혁,정명현_중소기업 다시 바라보기_썸네일_웹.jpg'
    me.pic= 'mimage/pic/강민혁,정명현_중소기업 다시 바라보기_보드_웹.jpg'
    me.youtube= 'https://www.youtube.com/embed/UNfkwcn09zY'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '류호경, 김선식'
    me.title= '창귀'
    me.description= '안예은의 ‘창귀’를 남성 유튜버 싱여가 커버한 곡이다. 무섭고 기괴하게 드로잉하여 노래의 분위기에 모션그래픽과 로토스코핑으로 작업하였고, 색감은 검은색과 빨간색으로 주워 원곡의 컨셉을 버리지 않고 한국의 전설을 보여주는 작품이다.'
    me.thumbnail= 'mimage/thum/류호경,-김선식_썸네일.jpg'
    me.pic= 'mimage/pic/류호경, 김선식_창귀.jpg'
    me.youtube= 'https://www.youtube.com/embed/Nh9KZtqOlzU'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '류호경'
    me.title= '낙원의 밤 예고편'
    me.description= '‘낙원의 밤’은 상대편 조직의 보스를 죽이는 핏빛 복수극을 그린 영화이다. 범죄물이기 때문에 무겁고 어두운 분위기를 주기위해 블랙바탕에 화이트 드로잉을 주었고, 포인트 레드를 사용해 인물간에 분위기를 조정한 로토스코핑 애니메이션이다.'
    me.thumbnail= 'mimage/thum/류호경_썸네일(1).jpg'
    me.pic= 'mimage/pic/류호경_낙원의 밤 예고편.jpg'
    me.youtube= 'https://www.youtube.com/embed/abt2JI0BVfU'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '류호경'
    me.title= 'I Love Kiss'
    me.description= '전 세계적인 인지도와 높은 인기를 보유하고 있는 안나수이의 립스틱 홍보 영상이다. 라인 일러스트로 로토스코핑과 모션그래픽으로 립스틱의 색을 강조하였고, 립스틱 색과 잘 어울릴 수 있는 꽃을 선정해 모션 그래픽 애니메이션으로 제작했다.'
    me.thumbnail= 'mimage/thum/류호경_썸네일.jpg'
    me.pic= 'mimage/pic/류호경_I Love Kiss.jpg'
    me.youtube= 'https://www.youtube.com/embed/B8nzbkuRuUA'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '정명현'
    me.title= '서울의 잠 못 이루는 밤'
    me.description= '10cm의 ‘서울의 잠 못 이루는 밤’을 키네틱 타이포로 제작했다. 통일감을 위해 노래의 분위기와 잘 어울리는 컬러를 사용하였고 가사에 어울리는 다양하고 부드러운 모션을 이용해 노래를 재미있게 풀어냈다.'
    me.thumbnail= 'mimage/thum/정명현_썸네일.jpg'
    me.pic= 'mimage/pic/정명현_서울의 잠 못 이루는 밤.jpg'
    me.youtube= 'https://www.youtube.com/embed/iGF3aunS1MI'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '박효정'
    me.title= '누구없소'
    me.description= '이 영상은 검은색과 밝은 베이지색, 그리고선을 메인으로 사용한 모션그래픽이다. 가사에 따라 어우러지는 일러스트와 기타의 리듬에 맞춰모션을 적용하였고 물결과 달의 일러스트를 중심으로 제작하였다.'
    me.thumbnail= 'mimage/thum/박효정_썸네일.jpg'
    me.pic= 'mimage/pic/박효정_누구없소.jpg'
    me.youtube= 'https://www.youtube.com/embed/Hj1weHU21E0'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '박주이, 원도윤'
    me.title= '중소기업 제대로 알리기'
    me.description= '대기업 같았던 빅히트 엔터테인먼트가 사실은 중소기업으로, 알고 있던 중소기업과는 전혀 다른 이미지다. 그래서 중소기업에 대해 제대로 알리기 위해 중소기업의 의미, 혜택을 자세히 알려 중소기업의 이미지를 개선하려고 한다.'
    me.thumbnail= 'mimage/thum/박주이, 원도윤_썸네일.jpg'
    me.pic= 'mimage/pic/박주이, 원도윤_중소기업제대로알리기.jpg'
    me.youtube= 'https://www.youtube.com/embed/9bVou7S6vO4'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '원도윤, 박주이'
    me.title= '옥탑방'
    me.description= '밴드 N.flying의 노래 옥탑방을 키네틱타이포로 만든 영상이다. 옥탑방은 옥상에 나란히 걸터앉아 함께 밤하늘을 보던 연인과 이별 후의 서정적인 감성을 담아낸 곡이다. 이러한 분위기를 표현하기 위해 3가지의 컬러로 키네틱타이포를 제작했다.'
    me.thumbnail= 'mimage/thum/원도윤, 박주이_썸네일.jpg'
    me.pic= 'mimage/pic/원도윤, 박주이_옥탑방.jpg'
    me.youtube= 'https://www.youtube.com/embed/pBqQbPtrvgU'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '신혜현'
    me.title= '카누'
    me.description= '상품 ‘카누’를 주제로 한 2D 애니메이션이다. 하루 중 가장 지친 시간인 오후 3시, 나만을 위해 준비된 작은 카페에서 카누 한 잔을 마시며 잠시나마 여행을 즐기듯 여유롭고 행복한 순간이 찾아온다는 것을 여행지로 표현했다.'
    me.thumbnail= 'mimage/thum/신혜현_썸네일(1).jpg'
    me.pic= 'mimage/pic/신혜현_카누.jpg'
    me.youtube= 'https://www.youtube.com/embed/aPtEwZ9suuk'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '신혜현'
    me.title= '놀이터'
    me.description= '이 영상은 놀이터에 있는 놀이 기구의 움직임을 모티브 한 모션그래픽이다. 도형과 선을 활용하여 역동적인 노래에 맞춰 활발한 움직임을 줌으로써 어렸을 때 놀이터에서 놀던 추억들이 생각나게끔 하는 요소가 담겨있다.'
    me.thumbnail= 'mimage/thum/신혜현_썸네일.jpg'
    me.pic= 'mimage/pic/신혜현_놀이터.jpg'
    me.youtube= 'https://www.youtube.com/embed/XZc-H7R3IvA'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '오동우'
    me.title= '스위트홈'
    me.description= 'Netflix 드라마 ‘스위트홈’을 레드 컬러와 블랙 컬러를 사용하여 강렬한 느낌을 주는 애니메이션으로 스위트홈의 등장인물들을 로토스코핑 기법과 핸드드로잉으로 제작하였다.'
    me.thumbnail= 'mimage/thum/오동우_썸네일.jpg'
    me.pic= 'mimage/pic/오동우_스위트홈.jpg'
    me.youtube= 'https://www.youtube.com/embed/BGnIvB1DZCo'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '신유찬'
    me.title= '우리는 변화한다'
    me.description= '중소기업이 제공하는 다양한 복지를 보여주며 사회적 책임, 근로자 노동 가치 존중, 훌륭한 직장 문화를 가지고 있다는 것을 보여주는 영상이다. 전체적인 색감을 통일해 편안함을 주었고, 공감 소재를 활용해 즐거움을 느낄 수 있도록 제작했다.'
    me.thumbnail= 'mimage/thum/신유찬_썸네일.png'
    me.pic= 'mimage/pic/신유찬_우리는 변화한다.jpg'
    me.youtube= 'https://www.youtube.com/embed/9nZCZ7gBsRg'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '김예지'
    me.title= '한복을 알리다'
    me.description= '우리나라의 한복을 알리기 위해 제작한 인포그래픽이다. 한복의 구성, 시대에 따른 형태, 상황 등에 따라 달라지는 한복을 보여주고 설명해준다.'
    me.thumbnail= 'mimage/thum/김예지_썸네일(1).jpg'
    me.pic= 'mimage/pic/김예지_한복을 알리다.jpg'
    me.youtube= 'https://www.youtube.com/embed/d4VK5Bx4By4'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '김예지'
    me.title= '중소기업의 힘'
    me.description= '우리나라의 중소기업 중 K-뷰티 중소기업에 중점을 두고 제작한 인포그래픽이다. K-뷰티 산업의 전체적인 흐름을 설명한 뒤, 어떠한 중소기업들이 있고 그 중소기업들은 어떤 기술을 가지고 발전해나가고 있는지 보여준다.'
    me.thumbnail= 'mimage/thum/김예지_썸네일.jpg'
    me.pic= 'mimage/pic/김예지_중소기업의 힘.jpg'
    me.youtube= 'https://www.youtube.com/embed/59pRk-t1SyM'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '전예린'
    me.title= '기묘한 이야기'
    me.description= '‘기묘한 이야기’는 80년대 미국을 배경으로 한 넷플릭스 시리즈의 오프닝 시퀀스 애니메이션이다. 스릴러 컨셉의 강렬함과 개성을 강조하기 위해 블랙과 레드 컬러로 통일감을 주었고, 핸드드로잉 기법을 이용해 표현했다.'
    me.thumbnail= 'mimage/thum/전예린_썸네일.jpg'
    me.pic= 'mimage/pic/전예린_기묘한 이야기(Stranger things).jpg'
    me.youtube= 'https://www.youtube.com/embed/Q6Up3ywUV5k'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '김나영'
    me.title= '새들이 울었던 자리가 있다'
    me.description= '주희 작가의 ‘새들이 울었던 자리가 있다’라는 시의 사람도 새처럼 삶의 고단함과 쉬어간다는 메시지를 새의 노래와 날개짓, 나무에서 쉬어가는 모습을 라인드로잉 기법으로 제작했다.'
    me.thumbnail= 'mimage/thum/김나영_썸네일.jpg'
    me.pic= 'mimage/pic/김나영_새들이 울었던 자리가 있다.jpg'
    me.youtube= 'https://www.youtube.com/embed/E3T-8ecSY-8'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '김나영, 한승희'
    me.title= '괜찮은 중소기업 어플'
    me.description= '‘참 괜찮은 중소기업 앱’을 홍보하고 많은 취업 준비생들과 청년들을 응원하기 위해 앱의 좋은 기능 4가지를 소개하며 함께 괜찮은 중소기업을 도전해 보자는 의미에서 인포그래픽을 제작한 영상이다.'
    me.thumbnail= 'mimage/thum/김나영,한승희_썸네일.jpg'
    me.pic= 'mimage/pic/김나영,한승희_참 괜찮은 중소기업 어플.jpg'
    me.youtube= 'https://www.youtube.com/embed/7T5Mm9_IL6Y'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '김다은'
    me.title= 'Luxury day'
    me.description= '밀튼 스텔리는 이태리의 시계 브랜드로 고풍스럽고 클래식한 디자인과 트랜드 패션 디자인 시계들이 함께 어우러져있다. 시계와 캐릭터들 간의 색상을 비슷하게 표현하여 화려하면서도 지나치게 튀지 않고 조화로워 보이도록 디자인했다.'
    me.thumbnail= 'mimage/thum/김다은, 홍성현_썸네일.jpg'
    me.pic= 'mimage/pic/김다은, 홍성현_Luxury Day.jpg'
    me.youtube= 'https://www.youtube.com/embed/7nwrVcz0u2A'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '안예은'
    me.title= 'SEASON'
    me.description= '계절의 특징을 나타내 언제든지 알맞은 의상을 골라 입을 수 있다는 것을 보여주었다. 변화를 크게 주기 위해 다양한 컬러를 사용하여 여러 의상과 계절별 풍경을 표현하였다.'
    me.thumbnail= 'mimage/thum/안예은_썸네일.jpg'
    me.pic= 'mimage/pic/안예은_SEASON.jpg'
    me.youtube= 'https://www.youtube.com/embed/nHKuzyh6QwM'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '정예림, 한승희'
    me.title= 'KARMA'
    me.description= 'AMPSTYLE과 초희가 결성한 프로젝트 밴드, 달의하루가 애니메이터 람다람과 콜라보한 노래이다. 아이보리, 네이비, 핑크 세 가지 색상만으로 심플하게 작업하였으며 간단한 오브제들을 사용하여 키네틱타이포로 역동적이게 제작하였다.'
    me.thumbnail= 'mimage/thum/정예림,한승희_썸네일.jpg'
    me.pic= 'mimage/pic/정예림,한승희_KARMA.jpg'
    me.youtube= 'https://www.youtube.com/embed/8RwotN3A7gA'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '홍성현, 김다은'
    me.title= '참 괜찮은 중소기업'
    me.description= '청년들의 구인구직이 어려운 가운데, 중소 벤처기업부에서 새롭게 선보이는 개인 맞춤형 구인구직 플랫폼인‘괜찮은 중소기업’사이트와 애플리케이션을 홍보하는 목적으로 제작한 인포그래픽 애니메이션이다.'
    me.thumbnail= 'mimage/thum/홍성현,김다은_썸네일.jpg'
    me.pic= 'mimage/pic/홍성현,김다은_참 괜찮은 중소기업.jpg'
    me.youtube= 'https://www.youtube.com/embed/I98vASNEjcg'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '무함마드 나우팔'
    me.title= 'LEVITATING'
    me.description= '이 곡의 가사는 사랑에 빠졌을 때 ‘Levitating’이라는 개념을 여러 우주 밖에서 언급하고 있다. 복고풍 느낌과 잘 어울리는 분홍색과 보라색으로 컬러를 선정하여 키네틱타이포그래피를 만들었다.'
    me.thumbnail= 'mimage/thum/나우팔_썸네일.jpg'
    me.pic= 'mimage/pic/나우팔_LEVITATING.jpg'
    me.youtube= 'https://www.youtube.com/embed/WEAAUC86Chs'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '적일적, 고벽영'
    me.title= 'THE LAZY SONG'
    me.description= '‘The Lazy Song’은 미국의 팝 가수 브루노 마스가 부른 노래이다. 현란한 색채와 역동적인 동작으로 그 곡을 연출했다. 해당 곡이 가진 발랄함과 빠른 리듬감을 표현했다.'
    me.thumbnail= 'mimage/thum/적일적,고벽영_썸네일.jpg'
    me.pic= 'mimage/pic/적일적,고벽영_THE LAZY SONG.jpg'
    me.youtube= 'https://www.youtube.com/embed/SMqvfELGV70'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '우삼청, 장함'
    me.title= 'Tik Tok'
    me.description= '틱톡은 요즘 유행하는 동영상 서비스로 많은 사람들이 이용한다. 이 동영상은 틱톡과 사람과의 관계, 사람들이 틱톡을 일상적으로 사용하는 방식으로 틱톡을 홍보한다.'
    me.thumbnail= 'mimage/thum/우삼청,장함 _썸네일.jpg'
    me.pic= 'mimage/pic/우삼청,장함 _Tik Tok.jpg'
    me.youtube= 'https://www.youtube.com/embed/s4dKYUAL5ZI'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    me = Work()
    me.artist= '국정, 임운유'
    me.title= 'Shape of you'
    me.description= '영국 남자 가수 에드시런이 부른 팝송이다. 영상 속 밝은 파란색과 빨간색으로 강조를 하고, 3D 모델링 기술과 핸드페인팅 기술이 적용되었으며 재미있는 그래픽 애니메이션이 많이 들어가 있어 재미있는 경험을 선사할 수 있다.'
    me.thumbnail= 'mimage/thum/국정,임운유_ 썸네일.jpg'
    me.pic= 'mimage/pic/국정,임운유_ shape of you.jpg'
    me.youtube= 'https://www.youtube.com/embed/qgcIfFiNRSE'
    me.wtype=Type.objects.get(wtype = 'me')
    media_list.append(me)

    for x in media_list:
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