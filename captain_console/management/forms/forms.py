from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, widgets
from users.models import Profile, UserAddress, UserCountry, UserCard
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from config.models import Config


class ConfigForm():
    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)

    hours_weekdays = forms.TextInput(attrs={'class': 'hours-weekdays', 'placeholder': 'Weekdays'})
    hours_saturday = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Saturday'})
    hours_sunday = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Sunday'})
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    telephone = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Telephone'})
    address = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Address'})
    social_facebook = forms.URLField(label='Facebook', required=False)
    social_twitter = forms.URLField(label='Twitter', required=False)
    social_youtube = forms.URLField(label='YouTube', required=False)
    social_instagram = forms.URLField(label='Instagram', required=False)
    about = forms.CharField(label='Um Okkur', widget=forms.Textarea(attrs={'rows': 9, 'cols':50, 'style':'resize:none;'}))
    location = forms.CharField(label='Staðsetning', max_length=999, widget=forms.TextInput())

    class Meta:
        model = Config
        fields = {
                'hours_weekdays', 
                'hours_saturday', 
                'hours_sunday', 
                'email', 
                'telephone', 
                'address',
                'social_facebook',
                'social_twitter',
                'social_youtube',
                'social_instagram'
                'about',
                'location'
            }

