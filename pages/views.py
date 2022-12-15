from django.views.generic import TemplateView
from comment.forms import CommentForm
from django.shortcuts import render, get_object_or_404
from comment.models import Comment

from posts.models import Post 



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



def  log_details_page(request):
    template_name = 'log.html'
    comments = Comment.objects.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'test': 1234,
                                        'comments': comments,
                                        'new_comment': new_comment,
                                        'comment_form': comment_form})