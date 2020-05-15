from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, widgets
from items.models import Item
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class EditItemForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":13,"cols":55,'style':'resize:none;'}))

    class Meta:
        model = Item
        fields = ('description', 'price')