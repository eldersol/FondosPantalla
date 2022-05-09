from django import forms
from fondo.models import Fondos


class FormularioFondo(forms.ModelForm):
    class Meta:
        model = Fondos
        fields = '__all__'
