from django.shortcuts import render
from django.views import generic
from .models import Setting
from apps.account.models import Account
from apps.portofolio.models import Category, Portofolio

def index(request):
    setting_list = Setting.objects.all()
    team_list   = Account.objects.all().order_by('role')
    porto_catlist = Category.objects.all()
    portofolio_list = Portofolio.objects.all()


    data = {
        'setting_list': setting_list,
        'team_list': team_list,
        'porto_catlist': porto_catlist,
        'portofolio_list': portofolio_list,
    }
    print (setting_list)
    return render(request, 'home.html',data)

def blog(request):
    return render(request, 'blog_detail.html')