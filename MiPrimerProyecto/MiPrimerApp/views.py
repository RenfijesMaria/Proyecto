from django.shortcuts import render
def MiPrimerFuncion(request):
    datos={
        'nombre':'Pablo'
    }
    return render(request, 'mi_primer_pagina.html',datos)
# Create your views here.
