from django.urls import path, include
from product2 import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]