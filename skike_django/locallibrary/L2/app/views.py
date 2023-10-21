from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def message(request,name,age):
    # name = request.GET.get('name', '')
    # age = request.GET.get('age', 10)
    return HttpResponse("Hello Django")

class Message(View):
    def get(self, request):
        return HttpResponse("Hello Django")