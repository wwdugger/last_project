from django.urls import path
from .views import HomePageView, RegisterPageView, PersonalInfoPageView, LocationPageView,SportPageView, PowerPageView

urlpatterns = [
    path('', HomePageView.as_view(), name= 'home'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('personal/', PersonalInfoPageView.as_view(), name='personal'),
    path('location/', LocationPageView.as_view(), name='location'),
    path('sport/', SportPageView.as_view(), name='sport'),
    path('power/', PowerPageView.as_view(), name='power'),

]