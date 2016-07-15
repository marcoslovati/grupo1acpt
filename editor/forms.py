from django import forms
from .models import Texto
# from django.forms import DateTimeField

class CadastroTextoForm(forms.ModelForm):
	
	# data_encontro = DateTimeField(widget=forms.widgets.DateTimeInput())
	
	class Meta:
		model = Texto
		fields = ('data_encontro', 'moderador_participa',)

