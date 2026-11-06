from django.shortcuts import render

def inicio(request):
    return render (request, "barcenas/templates/inicio.html")