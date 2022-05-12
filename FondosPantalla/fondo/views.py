import os
from pathlib import Path
from django.shortcuts import render
from fondo.forms import FormularioFondo
from django.http import HttpRequest
from fondo.models import Fondos
import ntpath
from PIL import Image


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

                #CAMBIAR TAMAÑO DE IMAGEN
                original = Image.open("./imgs/preview/" + imagen)
                preview = original.resize((136, 76))
                preview.save("./imgs/preview/" + imagen)
                download = original.resize((1366, 768))
                download.save("./imgs/download/" + imagen)

                #CONVERTIR A WEBP
                dire, extencion = os.path.splitext(imagen)
                for root, dirs, files in os.walk("./imgs/download/"):
                    for file in files:
                        if file.endswith(extencion):
                            archivo = os.path.join(root, file)
                            archivo_nuevo = archivo.replace(extencion, '.webp')
                            ima = Image.open(archivo).convert("RGB")
                            ima.save(archivo_nuevo, "webp")

            return render(request, "nuevo_fondo.html", {"form": form, "mensaje": "ok"})
        except Exception as e: print(e)

    def ver_datos(request, id):
        fondo = Fondos.objects.filter(id=id).first()
        titulo = fondo.titulo
        descripcion = fondo.descripcion
        precio = fondo.precio
        imagen = str(ntpath.basename(fondo.imagen.url))
        nombre_imagen = Path(imagen).stem
        nombre_imagen += ".webp"
        return render(request, "fondo.html", {"titulo": titulo, "imagen": nombre_imagen, "descripcion": descripcion, "precio": precio, "id": id})

    def listar(request):
        form = Fondos.objects.all()
        return render(request, "principal.html", {"form": form})

