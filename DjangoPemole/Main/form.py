from django import forms
from Main import models
from Main.models import Photo
from django.db import models
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    email = forms.EmailField(label='信箱')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
    password2 = forms.CharField(label='請再輸入一次密碼'
                                , widget=forms.PasswordInput())

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('密碼和確認密碼不同')
        return password2

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
