from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Texto
from .models import Usuario
from .forms import CadastroTextoForm

# Create your views here.

def inicial(request):
	textos_moderador = Texto.objects.filter(moderador=1).order_by('data_encontro') # trocar depois '1' pelo id do usuario logado
	textos_convidado = Texto.objects.filter(texto_usuario__usuario=1).exclude(moderador=1).order_by('data_encontro')
	return render(request, 'inicial.html', {'textos_moderador': textos_moderador, 'textos_convidado': textos_convidado})

def index(request):
    usuarios = Usuario.objects.all().order_by('nome')
    context = {'all_usuarios' : usuarios}
    return render(request, 'index.html', context)

def historia(request):
    historia = Texto.objects.filter()[:1].get()
    return render(request, 'historia.html', {'historia': historia})
		
def editar(request, pk):
    texto = get_object_or_404(Texto, pk=pk)
    return render(request, 'editar.html', {'texto': texto})

def incluir(request):
	if request.method == "POST":
		form = CadastroTextoForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.moderador = request.user
			post.save()
			return redirect('inicial')
	else:
		form = CadastroTextoForm()
	return render(request, 'incluir.html', {'form': form})