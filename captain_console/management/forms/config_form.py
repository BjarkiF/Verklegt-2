from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from footer.models import Footer
from django.contrib.auth.models import User
from django import forms


class ConfigForm(forms.ModelForm):
    hours_weekdays = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Weekdays'})
    hours_saturday = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Saturday'})
    hours_sunday = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Sunday'})
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    telephone = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Telephone'})
    address = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Address'})
    social_facebook = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Facebook'})
    social_twitter = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Twitter'})
    social_youtube = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Youtube'})
    social_instagram = forms.TextInput(attrs={'class': 'config-form', 'placeholder': 'Instagram'})

    #username = forms.TextInput(attrs={'class': 'register-form', 'placeholder': 'Notandanafn'})
    #first_name = forms.TextInput(attrs={'class': 'register-form', 'placeholder': 'Fornafn'})
    #last_name = forms.CharField()#widgets.TextInput(attrs={'class': 'register-form', 'placeholder': 'Eftirnafn'}))
    #email = forms.EmailField()#widgets.EmailInput(attrs={'class': 'register-form', 'placeholder': 'Netfang'}))
    #password1 = forms.CharField()#widgets.PasswordInput(attrs={'class': 'register-form', 'placeholder': 'Lykilorð'}))
    #password2 = forms.CharField()#widgets.PasswordInput(attrs={'class': 'register-form', 'placeholder': 'Staðfesta lykilorð'}))
    class Meta(forms.ConfigForm):
        model = User
        fields = ConfigForm.Meta.fields 
