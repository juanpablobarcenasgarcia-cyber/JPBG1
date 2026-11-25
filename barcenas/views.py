from django.shortcuts import render

def inicio (request):
    return render (request, "barcenas/inicio.html")

def registro(request):
    return render (request, "barcenas/formsregistro.html")
def musica(request):
    return render(request,"barcenas/fromsmusica.html")