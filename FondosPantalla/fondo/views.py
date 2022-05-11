import shutil

from django.shortcuts import render
from fondo.forms import FormularioFondo
from django.http import HttpRequest
from fondo.models import Fondos
import ntpath

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

                id = Fondos.objects.all().last().id
                fondo = Fondos.objects.filter(id=id).first()
                imagen = str(ntpath.basename(fondo.imagen.url))

                ruta = "./imgs/preview/" + imagen
                shutil.copy(ruta, "./imgs/download/" + imagen)

            return render(request, "nuevo_fondo.html", {"form": form, "mensaje": "ok"})
        except Exception as e: print(e)

    def ver_datos(request, id):
        fondo = Fondos.objects.filter(id=id).first()
        titulo = fondo.titulo
        descripcion = fondo.descripcion
        precio = fondo.precio
        imagen = str(ntpath.basename(fondo.imagen.url))

        return render(request, "fondo.html", {"titulo": titulo, "imagen": imagen, "descripcion": descripcion, "precio": precio})

    def listar(request):
        form = Fondos.objects.all()
        return render(request, "principal.html", {"form": form, "nombre": "emoji.png"})


    def descargar(request):
        print("descargar!!!!!!!")
        return render(request, "principal.html", {"form": ""})