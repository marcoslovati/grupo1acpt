from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from editor.models import Usuario

# Create your views here.

def index(request):
    usuarios = Usuario.objects.all().order_by('nome')
    context = {'all_usuarios' : usuarios}
    return render(request, 'index.html', context)