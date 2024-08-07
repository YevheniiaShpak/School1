from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_superuser = forms.BooleanField(required=False, label='Superuser')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superuser']


    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['is_superuser']:
            user.is_staff = True
            user.is_superuser = True
        if commit:
            user.save()
        return user