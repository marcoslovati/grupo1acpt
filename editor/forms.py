from django import forms
from .models import Texto
from .models import Usuario
# from django.forms import DateTimeField

class CadastroTextoForm(forms.ModelForm):
	
	# data_encontro = DateTimeField(widget=forms.widgets.DateTimeInput())
	
	class Meta:
		model = Texto
		fields = ('data_encontro', 'moderador_participa',)


class EdicaoTextoForm(forms.ModelForm):
	
	class Meta:
		model = Texto
		fields = ('tempo_participante', 'numero_rodadas', 'numero_linhas',)
