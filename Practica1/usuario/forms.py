# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuario.models import Userf


class SignUpForm(UserCreationForm):
    carrera= forms.CharField(max_length=30, required= True, help_text="Matemático o Físico.")
    CUI = forms.CharField(max_length=13,required=True)
    email = forms.EmailField(max_length=254,required=True)

    class Meta:
        model = Userf
        fields = ('username', 'carrera', 'CUI', 'email', 'password1', 'password2',)

    def guardar(self,commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.carrera = self.cleaned_data["carrera"]
        if commit:
            user.save()
        return user


class Edit_ProfileForm(UserChangeForm):
    class Meta:
        model= User
        fields =('email',)
