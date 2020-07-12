from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView
)
from .models import Study

# Function view
# def home(request):
#     context = {
#         'studies': Study.objects.all()
#     }
#     return render(request,'study_blog/home.html', context)



# def about(request):
#     return render(request,'study_blog/about.html')


#Class based views
class StudyListView(ListView):
    model = Study
    template_name = 'study_blog/home.html'
    context_object_name = 'studies'
    ordering = ['date_posted']


class StudyDetailView(DetailView):
    model = Study

class StudyCreateView(CreateView):
    model = Study
    fields = ['title', 'content', 'author']

class AboutView(ListView):
    model = Study
    template_name = 'study_blog/about.html'