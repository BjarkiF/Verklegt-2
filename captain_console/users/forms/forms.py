from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, widgets
from users.models import Profile, UserAddress, UserCountry, UserCard
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    username = forms.CharField(max_length=15)
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


class CheckoutAddressForm(EditAddressForm):
    street_name = forms.CharField(required=False)
    house_num = forms.CharField(required=False)
    city = forms.CharField(required=False)
    zipcode = forms.CharField(required=False)
    country_id = forms.ModelChoiceField(queryset=UserCountry.objects.all(), required=False)

    class Meta:
        model = UserAddress
        fields = ('street_name', 'house_num', 'city', 'zipcode', 'country_id' )


class UserCardForm(forms.ModelForm):
    name = forms.CharField(max_length=999)
    number = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'xxxx-xxxx-xxxx-xxxx'}), min_length=16,
                             max_length=16,) #validators=[RegexValidator(r'^\d{1,10}$')])
    exp_month = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'xx'}), min_length=2,
                             max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    exp_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'xx'}), min_length=2,
                             max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
    cvc = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'xxx'}), min_length=3,
                             max_length=3, validators=[RegexValidator(r'^\d{1,10}$')])

    class Meta:
        model = UserCard
        fields = ('number', 'exp_month', 'exp_year', 'cvc')