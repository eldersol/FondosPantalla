from django.shortcuts import render
from fondo.forms import FormularioFondo
from django.http import HttpRequest

# Create your views here.
class Fondo(HttpRequest):
    def inicio(request):
        form = FormularioFondo(request.POST)
        return render(request, "nuevo_fondo.html", {"form": form})

    def guardar(request):
        form = FormularioFondo(request.POST)
        form.save(commit=True)
        return render(request, "inicio.html", {"form": form, "mensaje": "ok"})





