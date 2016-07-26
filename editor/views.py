from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from .models import Texto
from .models import Usuario
from .forms import CadastroTextoForm
from .forms import EdicaoTextoForm

# Create your views here.

def inicial(request):
	usuario = request.session['usuario']
	textos_moderador = Texto.objects.filter(moderador=usuario).order_by('data_encontro')
	textos_convidado = Texto.objects.filter(texto_usuario__usuario=usuario).exclude(moderador=usuario).order_by('data_encontro')
	return render(request, 'inicial.html', {'textos_moderador': textos_moderador, 'textos_convidado': textos_convidado})

def index(request):
	if request.method == "POST":
		u_email = request.POST.get('email','')
		usuario = Usuario.objects.filter(email=u_email)[0]	
		if usuario is not None:
			request.session['usuario'] = usuario.id
			request.session['usuario_nome'] = usuario.nome
			return HttpResponseRedirect('/inicial')
	else:
		usuarios = Usuario.objects.all().order_by('nome')
		context = {'all_usuarios' : usuarios}
		return render(request, 'index.html', context)

def historia(request):
    historia = Texto.objects.filter()[:1].get()
    return render(request, 'historia.html', {'historia': historia})
		
def editar(request, pk):
	texto = get_object_or_404(Texto, pk=pk)
	form = EdicaoTextoForm(request.POST or None, instance=texto)
	if request.method == "POST":
		if form.is_valid():			
			form.save()
			return HttpResponseRedirect('/inicial')
	return render(request, 'editar.html', {'form': form})

def incluir(request):
	if request.method == "POST":
		form = CadastroTextoForm(request.POST)
		if form.is_valid():
			texto = form.save(commit=False)
			usuario_id = request.session['usuario']
			usuario = Usuario.objects.get(id=usuario_id)
			texto.moderador = usuario
			texto.encerrado = False
			texto.save()
			return HttpResponseRedirect('/inicial')
	else:
		form = CadastroTextoForm()
	return render(request, 'incluir.html', {'form': form})