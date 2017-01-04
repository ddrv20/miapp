from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime


def get_news(request):
    if request.method == 'POST':
        fecha = datetime.now()
        news = News.objects.filter(privilege=request.POST.get('privilege', 1), create_at__range=(date, datetime.now()))
        data = [new.as_json() for new in news]
        return JsonResponse({'data': data, 'success': 'true'})
    return JsonResponse({'success': 'false', 'reason': 'metodo no soportodo'})


def get_pppteg(request):
    pppTeg = PppTeg.objects.all()
    date = [pt.as_json2() for pt in pppTeg]
    return JsonResponse({'data': date}, safe=False)


def get_docs(request):
    docs = Docs.objects.all()
    date = [docu.as_json3() for docu in docs]
    return JsonResponse({'data': date}, safe=False)


def get_event(request):
    eve = Event.objects.all()
    date = [even.as_json4() for even in eve]
    return JsonResponse({'data': date}, safe=False)


def set_user(request):
    if request.method == 'POST':
        users = User.objects.all()
        for user in users:
            if user.email == request.POST.get('email'):
                return JsonResponse({'success': 'false', 'reason': 'El usuario que intenta guardar ya existe!'})
        if request.POST.get('typoUser', -1) == "1":
            User.objects.create(name=request.POST.get('name', -1), email=request.POST.get('email', -1), image=request.POST.get('image', -1), typoUser=request.POST.get('typoUser', -1), typoCarrer=request.POST.get('typoCareer', -1))
            return JsonResponse({'success': 'true'})
        if request.POST.get('typoUser', -1) == "2":
            User.objects.create(name=request.POST.get('name', -1), email=request.POST.get('email', -1), image=request.POST.get('image', -1), typoUser=request.POST.get('typoUser', -1), typoCarrer=0)
            return JsonResponse({'success': 'true'})
        return JsonResponse({'success': 'false', 'reason': 'Error con los parmetros de peticion'})
    return JsonResponse({'success': 'false', 'reason': 'Metodo no soportado'})