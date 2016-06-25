from django.db import models
from django.utils import timezone
import datetime

class Usuario(models.Model):
	nome = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	senha = models.CharField(max_length = 30)

	class Meta:
		db_table = 'Usuario'
		
class Genero(models.Model):
	nome = models.CharField(max_length = 100)
	
	class Meta:
		db_table = 'Genero'
		
class Texto(models.Model):
	data_encontro = models.DateTimeField()
	moderador = models.ForeignKey(Usuario)
	moderador_participa = models.BooleanField()
	titulo = models.TextField(max_length = 200)
	genero = models.ForeignKey(Genero)
	primeiro_paragrafo = models.TextField(max_length = 1000)
	tempo_participante = models.IntegerField()
	numero_rodadas = models.IntegerField()
	encerrado = models.BooleanField()
	
	class Meta:
		db_table = 'Texto'

class Texto_Usuario(models.Model):
	texto = models.ForeignKey(Texto)
	usuario = models.ForeignKey(Usuario)
	ordem = models.IntegerField()
	cancelado = models.BooleanField()
	
	class Meta:
		db_table = 'Texto_Usuario'
		
class Paragrafo(models.Model):
	texto = models.ForeignKey(Texto)
	usuario = models.ForeignKey(Usuario)
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	descricao = models.TextField(max_length = 1000)
    
	class Meta:
		db_table = 'Paragrafo'
		
class Tipo_Solicitacao(models.Model):
	descricao = models.CharField(max_length = 30)
		
class Solicitacao(models.Model):
	texto = models.ForeignKey(Texto)
	usuario = models.ForeignKey(Usuario)
	tipo = models.ForeignKey(Tipo_Solicitacao)
	rodada = models.IntegerField()
	atendida = models.BooleanField()
	
	class Meta:
		db_table = 'Solicitacao'	