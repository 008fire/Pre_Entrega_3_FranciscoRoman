from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    http_response = render(
        request = request,
        template_name= "base.html",
        context={},

    )
    return http_response

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response
