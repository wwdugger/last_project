
from django.urls import path 
from django import views


urlpatterns = [
path('<slug:slug>/', views.post_detail, name='pages/base')
]