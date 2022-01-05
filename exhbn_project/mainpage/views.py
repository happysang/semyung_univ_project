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
    allwork = Work.objects.all()
    return render (request, 'detailprofile.html', {'ppp':detail_obj, 'works':allwork})

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