from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('login')
