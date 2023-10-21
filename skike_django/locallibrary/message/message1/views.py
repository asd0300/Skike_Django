from django.shortcuts import render
from django.http import HttpResponse

def message(request,name,age):
    # name = request.GET.get('name', '')
    # age = request.GET.get('age', 10)
    return HttpResponse("Hello Django")
