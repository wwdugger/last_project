from django.views.generic import TemplateView

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

class NavBarPageView(TemplateView):
    template_name = "nav-bar.html"

