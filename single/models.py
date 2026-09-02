# models.py
from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    job_title = models.CharField(max_length=100, verbose_name="عنوان شغلی")
    bio = models.TextField(verbose_name="درباره من")
    email = models.EmailField(verbose_name="ایمیل")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    address = models.CharField(max_length=255, verbose_name="آدرس")
    birthday = models.DateField(verbose_name="تاریخ تولد")
    avatar = models.ImageField(upload_to='avatars/', verbose_name="تصویر پروفایل")

    def __str__(self):
        return self.full_name
