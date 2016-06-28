from django.shortcuts import render
from .models import Texto

# Create your views here.

def inicial(request):
	textos_moderador = Texto.objects.filter(moderador=1).order_by('data_encontro')
	textos_convidado = Texto.objects.filter(moderador=1).order_by('data_encontro')
	return render(request, 'inicial.html', {'textos_moderador': textos_moderador})