from ast import For
from cmath import infj
from django.shortcuts import redirect, render
from .forms import *
from CasqueApp.forms import *
from CasqueApp.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CasqueApp.forms import CForm
from django.core.mail import send_mail

def CView(request):

    if request.method=="POST":
        FormularioC=CForm(request.POST)

        if FormularioC.is_valid():

            infForm=FormularioC.cleaned_data

            send_mail(infForm['Asunto'], infForm['Mensaje'], infForm.get('email','laz.bertin@gmail.com'),['laz.bertin@gmail.com'])

            return render (request, 'ContactoSolicitado.html')
    else:
        FormularioC=CForm()

    return render (request, 'Contacto.html', {"form":FormularioC})

def index(request):
    return render(request, "index.html")

def Contacto(request):

    return render (request, 'Contacto.html')

def Experiencia(request):

    return render (request, 'Experiencia.html')

def NuestrosClientes(request):
    return render (request, 'NuestrosClientes.html')

def ContactoSolicitado(request):
    return render (request, 'ContactoSolicitado.html')

def Quienessomos(request):
    return render (request, 'Quienessomos.html')
