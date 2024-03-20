from django import forms
from base.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model =  Cadastro
        fields = ['nome', 'email', 'senha']
        widgets = {'senha': forms.PasswordInput()}
    # nome = forms.CharField()
    # email = forms.EmailField()
    # senha = forms.CharField(widget=forms.PasswordInput)