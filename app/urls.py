from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Resume',views.resume,name='resume'),
    path('contact',views.contact,name='contact'),
    path('project',views.project,name='project')
]
