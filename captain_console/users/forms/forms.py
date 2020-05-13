from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, widgets
from users.models import Profile, UserAddress, UserCountry
from django import forms
from django.contrib.auth.models import User

# TODO: PasswordResetForm klasa vantar.

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = 'Rangt notandanafn eða lykilorð!'

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'img')


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditAddressForm, self).__init__(*args, **kwargs)
        self.fields['country_id'].label_from_instance = lambda obj: "%s" % obj.country_name

    country_id = forms.ModelChoiceField(queryset=UserCountry.objects.all())

    class Meta:
        model = UserAddress
        fields = ('street_name', 'house_num', 'city', 'zipcode', 'country_id' )

# class EditCountryForm(forms.ModelForm):
#     country_select = forms.ModelChoiceField(queryset=UserCountry.objects.all(), initial=0)
#     class Meta:
#         model = UserCountry
#         fields = ('country_select',)