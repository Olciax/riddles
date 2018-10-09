from django import forms
from django.contrib.auth.models import User

from .models import MyUser


class MyUserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','email']

class RiddleAnswer(forms.Form):
    answer = forms.CharField(max_length=64,
                             widget=forms.TextInput(

                                 attrs = {

                                     'class': 'form-control',
                                     'style':'text-align:center;text-transform:uppercase',
                                     'placeholder': 'Podaj odpowiedź...',

                                 }
                             ))