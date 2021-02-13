from django.shortcuts import render
from .models import Portofolio
from apps.core.models import Setting

def portofolio_detail(request, slug):
    porto_detail = Portofolio.objects.get(slug=slug)
    set_list     = Setting.objects.all()


    data = {
        'porto_detail':porto_detail,
        'set_list': set_list
        
    }

    return render(request, 'portofolio_detail.html', data)