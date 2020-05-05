from django.forms import ModelForm, widgets
from users.models import Users
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Users
        exclude = ['id', 'user']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'img': widgets.TextInput(attrs={'class': 'form-control'})
        }