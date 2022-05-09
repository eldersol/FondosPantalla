from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():
    def home(self):
        home = get_template('inicio.html')
        return HttpResponse(home.render())

    def formulario(self):
        form = get_template('formulario.html')
        return HttpResponse(form.render())
