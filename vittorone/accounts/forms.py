from django import forms
from django.contrib.auth.forms import UserCreationForm

class NameForm(forms.Form):
    username = forms.CharField(label='Your name')
