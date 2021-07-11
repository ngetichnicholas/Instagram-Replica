from django import forms
from .models import Profile,Image,Comment
from django.contrib.auth.models import User



class SearchForm(forms.Form):
  search_field = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Search people...'}))

class PostForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['image','image_name','image_caption']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_photo','bio']

class CommentForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['comment'].widget=forms.TextInput()
    self.fields['comment'].widget.attrs['placeholder']='Add a comment...'
  class Meta:
    model = Comment
    fields = ('comment',)
