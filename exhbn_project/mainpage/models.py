from django.db import models


# Seokgeun - 작품 카테고리 모델 생성 12.21
class Type(models.Model):
    wtype=models.CharField(max_length = 10 , null = True)  # gr / ad / me 일단 3개로

    def __str__(self):
        return self.wtype

# Seokgeun - 작품 모델 생성 12.21
class Work(models.Model):
    title = models.CharField(max_length = 50) # 작품 제목
    artist = models.CharField(max_length= 50) # 창작자  창작자 여럿이라 외래키 뺌

    wtype = models.ForeignKey(Type, null=True, on_delete=models.CASCADE)  # 작품 타입 (Graphic, Advertise, Media)

    description = models.TextField(null=True) # 작품 설명

    # thumbnail = models.ImageField(null = True, upload_to="%Y/%m/%d")  # 작품 썸네일
    # pic = models.ImageField(null = True, upload_to="%Y/%m/%d")  # 작품 사진파일
    thumbnail = models.CharField(max_length=50)
    pic = models.CharField(max_length=50)

    # picprd = models.ImageField(null = True, blank = True, upload_to="%Y/%m/%d")  # 그래픽 전용 - 연출사진파일
    picprd = models.CharField(max_length=50)
    youtube = models.CharField(blank = True, null = True, max_length= 200) # 미디어 전용 - 유튜브 링크


    def __str__(self):
        return self.title
    
    
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=10,blank=True, null=True)
    pimage = models.CharField(max_length=20,blank=True, null=True)
    d_pimage = models.CharField(max_length=20,blank=True, null=True)
    eng_name = models.CharField(max_length=10,blank=True, null=True)
    introduce = models.TextField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=20,blank=True, null=True)
    wpage = models.CharField(max_length=100,blank=True, null=True)
    project = models.ForeignKey(Work, on_delete = models.CASCADE,blank=True, null=True)
