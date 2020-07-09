from django.shortcuts import render
from .models import Study


def home(request):
    context = {
        'studies': Study.objects.all()
    }
    return render(request,'study_blog/home.html', context)



def about(request):
    return render(request,'study_blog/about.html')
