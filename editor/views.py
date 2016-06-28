from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Texto
from .models import Usuario

# Create your views here.

def inicial(request):
	textos_moderador = Texto.objects.filter(moderador=1).order_by('data_encontro')
	textos_convidado = Texto.objects.filter(moderador=1).order_by('data_encontro')
	return render(request, 'inicial.html', {'textos_moderador': textos_moderador})

def index(request):
    usuarios = Usuario.objects.all().order_by('nome')
    context = {'all_usuarios' : usuarios}
    return render(request, 'index.html', context)