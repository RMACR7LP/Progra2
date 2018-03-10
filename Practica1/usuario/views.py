# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm , UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from usuario.forms import SignUpForm, Edit_ProfileForm
from django.contrib.auth.models import User 
from .models import Userf

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data = request.POST) # <- vid 21, 'request.POST is not the first parameter'
        args = {'user':request.user}
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect ('profile',user.username)
    else:
        form= AuthenticationForm()
    return render(request, 'usuario/acceso.html', {'form':form})
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            x= form.save(commit=False)
            x.save()
            subject= 'Email de Confirmación'
            message= 'Este correo se mandó para confirmar el registro de un usuario'
            from_email=settings.EMAIL_HOST_USER
            to_list=[x.email,settings.EMAIL_HOST_USER]
            #send_mail(subject, message, from_email,to_list, fail_silently=True)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'usuario/signup.html', {'form': form})

def perfil_view(request,username):
        z= get_object_or_404(Userf, pk=username)
        text= {'user': z}
        return render(request,'usuario/perfil.html', text)


def edit_perfil(request):
    if request.method == 'POST':
        form = Edit_ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            user=request.user.get_user()
            return redirect('profile', user.username)
    else:
        form= Edit_ProfileForm(instance =request)
        arg= {'form':form}
        return render(request,'usuario/edit_perfil.html',arg)
        