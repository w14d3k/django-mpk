from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import UserPurchasediTcketsList
import datetime


User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    # A form for creating new users. Includes all the required fields, plus a repeated password.
    first_name = forms.CharField(label='Imię', widget=forms.TextInput)
    last_name = forms.CharField(label='Nazwisko', widget=forms.TextInput)
    email = forms.EmailField(label='Email')
    pesel = forms.CharField(label='Pesel', widget=forms.TextInput, validators=[RegexValidator(r'^\d\d\d\d\d\d\d\d\d\d\d$')])
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'pesel')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Wpisane hasła się różnią")
        else:
            password_validation.validate_password(password1)
            password_validation.validate_password(password2)
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    # A form for updating users. Includes all the fields on
    # the user, but replaces the password field with admin's
    # password hash display field.
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'pesel', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    
    username = forms.EmailField(label='Email', help_text='Twój email')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    is_remembered = forms.BooleanField()


class RegisterForm(forms.ModelForm):
    
    first_name = forms.CharField(label='Imię', widget=forms.TextInput)
    last_name = forms.CharField(label='Nazwisko', widget=forms.TextInput)
    email = forms.EmailField(label='Email')
    pesel = forms.CharField(label='Pesel', widget=forms.TextInput, validators=[RegexValidator(r'^\d\d\d\d\d\d\d\d\d\d\d$')])
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput, help_text='Twoje hasło')
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)
    is_terms_accepted = forms.BooleanField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'pesel', 'is_terms_accepted',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Wpisane hasła się różnią")
        else:
            password_validation.validate_password(password1)
            password_validation.validate_password(password2)
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active=True
        if commit:
            user.save()
        return user
    
class TicketPurchaseForm(forms.ModelForm):
    
    lines = forms.CharField(max_length=255, widget=forms.TextInput)
    
    class Meta:
        model = UserPurchasediTcketsList
        fields = ( 'lines',)

    