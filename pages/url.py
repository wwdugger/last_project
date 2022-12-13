from django.urls import path
from . import views
from django.urls import path
from .views import( 
LoginPageView, 
RegisterPageView, 
PersonalInfoPageView, 
LocationPageView,
SportPageView, 
PowerPageView, 
ProfilePageView, 
RunPageView, 
HomePageView, 
AboutPageView,
LogsPageViews,
FiveKPageViews,
ProgramsPageViews,
IndexPageViews,
)

from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginPageView.as_view(), name= 'login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('personal/', PersonalInfoPageView.as_view(), name='personal'),
    path('location/', LocationPageView.as_view(), name='location'),
    path('sport/', SportPageView.as_view(), name='sport'),
    path('power/', PowerPageView.as_view(), name='power'),
    path('run/', RunPageView.as_view(), name='run'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html')),
    path('home/', HomePageView.as_view(), name='home'),
    path('index/', IndexPageViews.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('log/', LogsPageViews.as_view(), name="logs"),
    path('5k_run/', FiveKPageViews.as_view(), name="5k_run"),
    path('programs/', ProgramsPageViews.as_view(), name="programs"),
    #signup#
    #path('register/', views.sign_up, name='register'),
]

