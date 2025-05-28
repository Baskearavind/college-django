from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('faculty/', views.faculty, name='faculty'),
    path('students/', views.students, name='students'),
    path('contact/', views.contact, name='contact'),
]
