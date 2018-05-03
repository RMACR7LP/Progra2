# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from PIL import Image
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm , UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from usuario.forms import SignUpForm , TextForm
from django.contrib.auth.models import User 
from usuario.models import Texto



def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data = request.POST) # <- vid 21, 'request.POST is not the first parameter'
        args = {'user':request.user}
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect ('profile', user)
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
            send_mail(subject, message, from_email,to_list, fail_silently=True)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'usuario/signup.html', {'form': form})

def perfil_view(request,username):
    z= User.objects.get(username=username)
    text= {'user': z}
    if request.method=='POST':
        return redirect('textos')
    return render(request,'usuario/perfil.html', text)
        

def textos_view(request):
    textos=Texto.objects.filter(autor=request.user.username)   
    if request.method=='POST' and 'Subir Texto' in request.POST:
        return redirect('subir') # recordar que aquí en vez de 'display' va 'subir')
    elif request.method=='POST' and 'Mostrar Texto' in request.POST:
        return redirect('display')
    return render(request, 'usuario/Textos.html', {'data': textos})
    

def subir_texto_view(request):
    if request.method == 'POST':
        form = TextForm(request.POST, request.FILES)
        if form.is_valid():
            x=form.save()
            return redirect('textos')
    else:
        form= TextForm()
    return render(request, 'usuario/subir.html', {'form':form})


#-------------------------Funciones del autómata----------------------------------------
list=[]
Digitos = ['0','1','2','3','4','5','6','7','8','9']
alfabeto =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','ñ','á','é','í','ó','ú','Á','É','Í','Ó','Ú']
reservadas={"teorema","Matemático","Matemática", "Hilbert", "Turing","análisis","Euler","Fermat","Pitágoras","autómata","Boole","Cantor","Perelman","Experimentación","Físico","Física","Astronomía","Mecánica","Newton","Einstein","Galileo","Modelo","Tesla","Dinámica","Partículas"}

states = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','ñ','á','é','í','ó','ú','Á','É','Í','Ó','Ú','0','1','2','3','4','5','6','7','8','9'}
finales = {'¿',')','?',',',' ','!', ':', ';','(','¡'}

tf = dict()
for d in Digitos:
    tf[(0,d)] = 2
    tf[(1,d)] = 2
    tf[(2,d)] = 2
    tf[(3,d)] = 6
    tf[(6,d)] = 6
    tf[(5,d)] = 8
    tf[(8,d)] = 8
    tf[(10,d)] = 13
    tf[(12,d)] = 14
    tf[(13,d)] = 13
    tf[(14,d)] = 14
    tf[(15,d)] = 14
for a in alfabeto:
    tf[(0,a)] = 16
    tf[(16,a)] = 16
tf[(0,'-')] = 1
tf[(2,'.')] = 3
tf[(2, '*')] = 4
tf[(2, '+')] = 5
tf[(2, '-')] = 5
tf[(2,'i')] = 11
tf[(4, '1')] = 7
tf[(6, '*')] = 4
tf[(6, '+')] = 5
tf[(6, '-')] = 5
tf[(7, '0')] = 9
tf[(8,'.')] = 10
tf[(8, 'i')] = 11
tf[(9, '^')] = 12
tf[(12,'-')] = 15
tf[(13,'i')] = 11

start_state = 0
accept_states = { 2, 6, 11, 14, 16}


class DFA:
    current_state = None
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return
    
    def in_accept_state(self):
        return self.current_state in accept_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        temporal=''
        texto_analizado=''
        for caracter in input_list:
            if caracter in finales: 
                if self.current_state==11:  #En: Azul, Re: Verde, NC; Morado; Complejos; Rojos, palabras; Gris
                    texto_analizado=texto_analizado+'<font color=red>'+temporal+'</font>'+caracter
                elif self.current_state==2:
                    texto_analizado=texto_analizado+'<font color=blue>'+temporal+'</font>'+caracter
                elif self.current_state==14: 
                    texto_analizado=texto_analizado+'<font color=purple>'+temporal+'</font>'+caracter
                elif self.current_state==6: 
                    texto_analizado=texto_analizado+'<font color=green>'+temporal+'</font>'+caracter
                elif self.current_state==16: 
                    if temporal in reservadas:
                        texto_analizado=texto_analizado+'<font color=gray>'+temporal+'</font>'+caracter
                        if temporal in list:
                            pass 
                        else:
                            list.append(temporal)
                    else:
                        texto_analizado=texto_analizado+temporal+caracter
                else: 
                    texto_analizado=texto_analizado+temporal+caracter
                temporal=''
                self.go_to_initial_state() 
            else:
                temporal=temporal+caracter
                self.transition_to_state_with_input(caracter)


        if self.current_state==11:  
            texto_analizado=texto_analizado+'<font color=red>'+temporal+'</font>'+caracter
        elif self.current_state==2:
            texto_analizado=texto_analizado+'<font color=blue>'+temporal+'</font>'+caracter
        elif self.current_state==14: 
            texto_analizado=texto_analizado+'<font color=purple>'+temporal+'</font>'+caracter
        elif self.current_state==6: 
            texto_analizado=texto_analizado+'<font color=green>'+temporal+'</font>'+caracter
        elif self.current_state==16: 
            if temporal in reservadas:
                texto_analizado=texto_analizado+'<font color=gray>'+temporal+'</font>'+caracter
                if temporal in list:
                    pass
                else:
                    list.append(temporal)
            else:
                texto_analizado=texto_analizado+temporal+caracter
        else: 
            texto_analizado=texto_analizado+temporal+caracter
            temporal=''
            self.go_to_initial_state() 

        texto_analizado=texto_analizado
        return texto_analizado

d = DFA(states, alphabet, tf, start_state, accept_states)

#cadena= ''
#for i in cadena_limpia.split():
#    d.run_with_input_list(list(i))
#    if d.run_with_input_list(list(i))==2:
#        print 'Entero'
#        for i in cadena:
#            cadena.replace(i,"<font color=red>"+i+"</font>")
#    elif d.run_with_input_list(list(i))==6: 
#        print 'Real'
#    elif d.run_with_input_list(list(i))==11:
#        print 'Complejo'
#    elif d.run_with_input_list(list(i))==14:
#        print 'Notación Científica'
#    elif d.run_with_input_list(list(i))==16:
#        print 'palabra'
#    else:
#        print False
#--------------------------------------------------------------------------------------
path= os.getcwd()
def display_texto_view(request):
    documento = Texto.objects.get(nombre='doc2')
    x_file= open(path +"\media\\textos\\"+ 'doc2' +".pdf","r")
    data= '<l>Alan Mathison <span style="color: #808B96">Turing</span>, OBE (Paddington, Londres, <span style="color: #0000FF">23</span> de junio de 1912-Wilmslow, Cheshire, <span style="color: #0000FF">7</span> de junio de <span style="color: #0000FF">1954</span>), fue un matem├ítico, l├│gico, cient├¡fico de la computaci├│n, cript├│grafo, fil├│sofo, maratoniano y corredor de ultra distancia brit├ínico. Es considerado uno de los padres de la ciencia de la computaci├│n y precursor de la inform├ítica moderna. Proporcion├│ una influyente formalizaci├│n de los conceptos de algoritmo y computaci├│n: la m├íquina de Turing. Formul├│ su propia versi├│n de la hoy ampliamente aceptada tesis de Church-Turing (<span style="color: #0000FF">1936</span>).</l>'
    texto_analizado=d.run_with_input_list(data)
    personas =[]
    for i in list:
        personas.append(str(i)+".jpg")
    print personas
    return render(request, 'usuario/documento.html', {'data':texto_analizado, 'images':personas})





