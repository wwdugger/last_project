from django.urls import path
from .views import LoginPageView, RegisterPageView, PersonalInfoPageView, LocationPageView,SportPageView, PowerPageView, ProfilePageView, RunPageView, NavBarPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name= 'login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('personal/', PersonalInfoPageView.as_view(), name='personal'),
    path('location/', LocationPageView.as_view(), name='location'),
    path('sport/', SportPageView.as_view(), name='sport'),
    path('power/', PowerPageView.as_view(), name='power'),
    path('run/', RunPageView.as_view(), name='run'),
    path('profile/', ProfilePageView.as_view(), name='pofile'),
    path('nav-bar/', NavBarPageView.as_view(), name='navbar'),

]
