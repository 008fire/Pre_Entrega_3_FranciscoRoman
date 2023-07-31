from django import forms


class ArticuloFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    marca = forms.CharField(required=True, max_length=64)
    precio = forms.IntegerField(required=True, max_value=50000)
