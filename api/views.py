from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


def get_news(request):
    news = News.objects.all()
    data = [new.as_json() for new in news]
    return JsonResponse({'data': data}, safe=False)
