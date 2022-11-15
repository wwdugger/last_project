from django.views.generic import TemplateView

class HomePageView(TemplateView):
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