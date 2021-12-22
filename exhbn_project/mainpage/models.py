from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=10)
    eng_name = models.CharField(max_length=10)
    introduce = models.TextField(max_length=100)
    email = models.EmailField(max_length=20)
    wpage = models.CharField(max_length=100)

# Seokgeun - 작품 카테고리 모델 생성 12.21
class Type(models.Model):
    wtype=models.CharField(max_length = 10 , null = True)  # gd / ad / media 일단 3개로

# Seokgeun - 작품 모델 생성 12.21
class Work(models.Model):
    title = models.CharField(max_length = 50) # 작품 제목
    artist = models.CharField(max_length= 50) # 창작자  창작자 여럿이라 외래키 뺌

    wtype = models.ForeignKey(Type, null=True, on_delete=models.CASCADE)  # 작품 타입 (Graphic, Advertise, Media)

    description = models.TextField(null=True) # 작품 설명
    pic = models.ImageField(null = True, upload_to="%Y/%m/%d")  # 작품 사진파일
    youtube = models.CharField(max_length= 200) # 유튜브 링크

