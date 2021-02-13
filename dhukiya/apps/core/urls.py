from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('blog-detail/', views.blog, name='blog_detail')
    
]