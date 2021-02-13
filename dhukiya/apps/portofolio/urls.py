from django.urls import path
from . import views
urlpatterns = [
    path('portofolio-detail/<slug:slug>/', views.portofolio_detail, name='portofolio_detail')
]