from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

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



# class SignUpForm(forms.Form):
#     username = forms.CharField(max_length=64, label='Nazwa użytkownika')
#     password = forms.CharField(max_length=64, label='Hasło', validators=[validate_password], widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=64, label='Potwierdź hasło', widget=forms.PasswordInput)
#
#     def clean(self):
#         cleaned_data = super(SignUpForm, self).clean()
#         password = cleaned_data.get('password')
#         password2 = cleaned_data.get('password2')
#
#         if password != password2:
#             raise forms.ValidationError('Podano różne hasła')


class UserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args,**kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None