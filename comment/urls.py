
from django.urls import path 
from . import views


urlpatterns = [
path('<slug:slug>/', views.post_detail, name='pages/base'),
path('test/details', views.post_detail, name="pages/test")
]