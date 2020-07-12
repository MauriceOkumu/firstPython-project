from django.urls import path
from .views import (
    StudyListView, 
    AboutView,
    StudyDetailView, 
    StudyCreateView
)
# from . import views

urlpatterns = [
    # path('', views.home, name='study-home'),
    path('', StudyListView.as_view(), name='study-home'),
    # path('about/', views.about, name='study-about'),
    path('about/', AboutView.as_view(), name='study-about'),
     path('study/new/', StudyCreateView.as_view(), name='study-create'),
    path('study/<int:pk>/', StudyDetailView.as_view(), name='study-detail'),
]
