from django.contrib import admin
from django.urls import path
from .views import Message

urlpatterns = [
    # path('', message)
    path('message', Message.as_view())
]
