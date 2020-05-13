from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from users.models import Profile
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    username = forms.TextInput(attrs={'class': 'register-form', 'placeholder': 'Notandanafn'})
    first_name = forms.TextInput(attrs={'class': 'register-form', 'placeholder': 'Fornafn'})
    last_name = forms.CharField()#widgets.TextInput(attrs={'class': 'register-form', 'placeholder': 'Eftirnafn'}))
    email = forms.EmailField()#widgets.EmailInput(attrs={'class': 'register-form', 'placeholder': 'Netfang'}))
    password1 = forms.CharField()#widgets.PasswordInput(attrs={'class': 'register-form', 'placeholder': 'Lykilorð'}))
    password2 = forms.CharField()#widgets.PasswordInput(attrs={'class': 'register-form', 'placeholder': 'Staðfesta lykilorð'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
