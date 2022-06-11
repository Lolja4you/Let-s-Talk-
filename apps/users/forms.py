from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from users.models import CustomUsers

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUsers
        fields = ('email', 'username', 'password1', 'password2')




class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsers
        fields = ('email',)