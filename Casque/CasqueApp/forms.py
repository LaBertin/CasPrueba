from django import forms

class CForm(forms.Form):

    Nombre=forms.CharField()
    Correo=forms.EmailField()
    Asunto=forms.CharField()
    Mensaje=forms.CharField()