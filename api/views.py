from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


def get_news(request):
    news = News.objects.all()
    data = [new.as_json() for new in news]
    return JsonResponse({'data': data}, safe=False)


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
