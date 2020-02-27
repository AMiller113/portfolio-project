from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blog_home'),
    path('<int:blog_id>/',  views.blog_detail, name='blog_detail')
]
