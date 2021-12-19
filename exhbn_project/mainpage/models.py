from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=10)
    eng_name = models.CharField(max_length=10)
    introduce = models.TextField(max_length=100)
    email = models.EmailField(max_length=20)
    wpage = models.CharField(max_length=100)
