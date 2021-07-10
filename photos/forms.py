from django import forms

class SearchForm(forms.Form):
    search_field = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Search people...'}))