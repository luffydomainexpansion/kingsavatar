from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chapter/<int:chapter_number>/', views.read_chapter, name='read_chapter'),
]

