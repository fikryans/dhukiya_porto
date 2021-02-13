from django.shortcuts import render
from .models import Account

def teamList(request):
    objteam =   Account.objects.all()

    data = {
        'objteam':objteam
    }

    return render(request, 'team.html', data)