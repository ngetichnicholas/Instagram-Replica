from django import forms
from .models import Profile,Image,Comment


class SearchForm(forms.Form):
  search_field = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Search people...'}))

class PostForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude =['likes','profile']

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude=['username']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['photo', 'comment_username']