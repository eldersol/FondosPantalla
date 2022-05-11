from django.shortcuts import render
from fondo.forms import FormularioFondo
from django.http import HttpRequest
from fondo.models import Fondos

# Create your views here.
class Fondo(HttpRequest):
    def inicio(request):
        form = FormularioFondo()
        return render(request, "nuevo_fondo.html", {"form": form})

    def guardar(request):
        try:
            form = FormularioFondo(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return render(request, "nuevo_fondo.html", {"form": form, "mensaje": "ok"})
        except Exception as e: print(e)

    def ver_datos(request, id):
        fondo = Fondos.objects.filter(id=id).first()
        #form = FormularioFondo(instance=fondo)
        titulo = fondo.titulo
        descripcion = fondo.descripcion
        precio = fondo.precio
        imagen = fondo.imagen

        return render(request, "fondo.html", {"titulo": titulo, "imagen": imagen, "descripcion":descripcion, "precio":precio})

    def listar(request):
        form = Fondos.objects.all()
        return render(request, "principal.html", {"form": form})




