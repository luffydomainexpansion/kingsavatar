from django.urls import path
from . import views

urlpatterns = [
    path('chapter/<int:number>/', views.read_chapter, name='read_chapter'),
]
