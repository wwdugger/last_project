from django.views.generic import TemplateView 

#from .forms import LoginForm, RegisterForm
#from django import forms
#from django.shortcuts import render, redirect
#from django.contrib import messages
#from django.contrib.auth import login, authenticate, logout


class LoginPageView(TemplateView):
    template_name = "login.html"

class RegisterPageView(TemplateView):
    template_name = "register.html"

class PersonalInfoPageView(TemplateView):
    template_name = "personal_info.html"

class LocationPageView(TemplateView):
    template_name = "location.html"

class SportPageView(TemplateView):
    template_name = "sport.html"

class PowerPageView(TemplateView):
    template_name = "power.html"

class RunPageView(TemplateView):
    template_name = "run.html"

class ProfilePageView(TemplateView):
    template_name = "profile.html"

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class LogsPageViews(TemplateView):
    template_name = 'log.html'

class FiveKPageViews(TemplateView):
    template_name = '5k_run.html'

class ProgramsPageViews(TemplateView):
    template_name = 'programs.html'

class IndexPageViews(TemplateView):
    template_name = 'index.html'

#signup#
#class LoginForm(forms.Form):
#    username = forms.CharField(max_length=65)
#   password = forms.CharField(max_length=65, widget=forms.PasswordInput)

##def sign_up(request):
#    if request.method == 'GET':
#        form = RegisterForm()
#        return render(request, 'pages/register.html', { 'form': form})

#    if request.method == 'POST':
#        form = RegisterForm(request.POST) 
#        if form.is_valid():
#            user = form.save(commit=False)
#           user.username = user.username.lower()
#          user.save()
#         messages.success(request, 'You have singed up successfully.')
#        login(request, user)
#       return redirect('posts')
#  else:
#     return render(request, 'pages/register.html', {'form': form})
