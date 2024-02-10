from django import forms
from .models import *

class FanForm(forms.ModelForm):
    class Meta:
        model=Fan
        fields='__all__'

class KursForm(forms.Form):
    nom=forms.CharField(label='Nom:')
    daraja = forms.CharField(label='Daraja:')
    narx = forms.IntegerField(label='Narx:')
    chegirma = forms.CharField(label='Chegirma:')

class UstozForm(forms.Form):
    ism=forms.CharField(label='ism')
    familiya = forms.CharField(label='familiya')
    jinsi = forms.CharField(label='jinsi')
    yosh = forms.IntegerField(label='yosh')



