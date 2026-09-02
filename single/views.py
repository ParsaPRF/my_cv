from django.shortcuts import render


def home(request):
    return render(request, "single/home.html")

# views.py
from django.shortcuts import render
from .models import Profile

from django.shortcuts import render

def resume_view(request):
    # Defining profile information directly in python code without database
    profile = {
        'full_name': 'امیرپارسا فتح الهی',
        'job_title': 'توسعه‌دهنده وب',
        'email': 'parsatf98@gmail.com',
        'phone': '+98 919 213 6163',
        'birthday': '۲۱ آبان ۱۳۸۳',
        'address': 'تهران، ایران',
        'bio': 'من یک توسعه‌دهنده وب با سابقه کار روی پروژه‌های مختلف هستم. به زبان پایتون و فریم‌ورک جنگو تسلط دارم و علاقه‌مند به یادگیری تکنولوژی‌های جدید هستم.',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'instagram': 'https://instagram.com',
    }
    
    context = {
        'profile': profile
    }
    return render(request, 'single/home.html', context)


