from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, Profile
from django.utils.translation import gettext as _

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter full name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "example@gmail.com"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "+383(49)123123"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Confirm password"}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords do not match"))

        return password2

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Create a related profile
            Profile.objects.create(user=user)
        return user