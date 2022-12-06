from django import forms
from posts.models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(width=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter Comment'}), required=True)


    class Meta:
        model = Comment
        fields = ['body']