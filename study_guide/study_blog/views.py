from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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
    paginate_by = 2


class StudyDetailView(DetailView):
    model = Study

class StudyCreateView(CreateView):
    model = Study
    fields = ['title', 'content', 'author']

class StudyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Study
    fields = ['title', 'content', 'author']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class StudyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Study
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

  

class AboutView(ListView):
    model = Study
    template_name = 'study_blog/about.html'