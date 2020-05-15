from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, widgets
from users.models import Profile, UserAddress, UserCountry, UserCard
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from config.models import Config


class ConfigForm(forms.Form):
    c = Config.objects.last()

    def __init__(self, *args, **kwargs):
        c = Config.objects.last()
        super(ConfigForm, self).__init__(*args, **kwargs)
        self.fields['about'].initial = c.about

    hours_weekdays = forms.CharField(label='Virkir dagar', required=False, widget=forms.TextInput(attrs={'class': 'form-weekdays', 'value': c.hours_weekdays}))
    hours_saturday = forms.CharField(label='Laugardagar', required=False, widget=forms.TextInput(attrs={'class': 'form-weekdays', 'value': c.hours_saturday}))
    hours_sunday = forms.CharField(label='Sunnudagar', required=False, widget=forms.TextInput(attrs={'class': 'form-weekdays', 'value': c.hours_sunday}))
    email = forms.EmailField(label='Tölvupóstfang', widget=forms.EmailInput(attrs={'class': 'form-email', 'placeholder': '', 'value': c.email}))
    telephone = forms.CharField(label='Telephone', required=False, widget=forms.TextInput(attrs={'class': 'form-telephone', 'value': c.telephone}))
    address = forms.CharField(label='Address', required=False, widget=forms.TextInput(attrs={'class': 'form-address', 'value': c.address}))
    social_facebook = forms.URLField(label='Facebook', required=False, widget=forms.TextInput(attrs={'class': 'form-facebook', 'value': c.social_facebook}))
    social_twitter = forms.URLField(label='Twitter', required=False, widget=forms.TextInput(attrs={'class': 'form-twitter', 'value': c.social_twitter}))
    social_instagram = forms.URLField(label='Instagram', required=False, widget=forms.TextInput(attrs={'class': 'form-instagram', 'value': c.social_instagram}))
    about = forms.CharField(label='Um Okkur', widget=forms.Textarea(attrs={'rows': 20, 'cols':50, 'style':'resize:none;', 'class':'form-about'}))
    location = forms.CharField(label='Staðsetning', max_length=999, widget=forms.TextInput(attrs={'class': 'form-about', 'value': c.location}))
    lat = forms.CharField(label='Breiddargráða', widget=forms.TextInput(attrs={'class': 'form-about', 'value': c.lat}))
    long = forms.CharField(label='Lengdargráða', widget=forms.TextInput(attrs={'class': 'form-about', 'value': c.long}))
    zoom = forms.CharField(label='Zoom', widget=forms.TextInput(attrs={'class': 'form-about', 'value': c.zoom}))

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
                'social_instagram'
                'about',
                'location'
            }

