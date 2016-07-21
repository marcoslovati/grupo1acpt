from django.db import models
from django.utils import timezone
import datetime

class Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	senha = models.CharField(max_length = 30)
	
	class Meta:
		db_table = 'Usuario'
		
class Genero(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length = 100)
	
	class Meta:
		db_table = 'Genero'
		
class Texto(models.Model):
	id = models.AutoField(primary_key=True)
	data_encontro = models.DateTimeField("Data primeiro encontro")
	moderador = models.ForeignKey(Usuario)
	moderador_participa = models.BooleanField()
	titulo = models.TextField(max_length = 200, null = True, blank = True)
	genero = models.ForeignKey(Genero, null = True, blank = True)
	primeiro_paragrafo = models.TextField(max_length = 1000, null = True, blank = True)
	tempo_participante = models.IntegerField(null = True, blank = True)
	numero_rodadas = models.IntegerField(null = True, blank = True)
	encerrado = models.BooleanField()
	rodada_atual = models.IntegerField(null = True, blank = True)
	numero_linhas = models.IntegerField(null = True, blank = True)
	
	class Meta:
		db_table = 'Texto'

class Texto_Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	texto = models.ForeignKey(Texto)
	usuario = models.ForeignKey(Usuario)
	ordem = models.IntegerField()
	cancelado = models.BooleanField()
	
	class Meta:
		db_table = 'Texto_Usuario'
		
class Paragrafo(models.Model):
	id = models.AutoField(primary_key=True)
	texto = models.ForeignKey(Texto)
	usuario = models.ForeignKey(Usuario)
	data_inicio = models.DateTimeField(null = True)
	data_fim = models.DateTimeField(null = True)
	descricao = models.TextField(max_length = 1000)
    
	class Meta:
		db_table = 'Paragrafo'
		
TIPO_SOLICITACAO_OPCOES = (
    ('V', 'Passar a vez'),
    ('P', 'Pular rodada'),
)
		
# class Tipo_Solicitacao(models.Model):
	# descricao = models.CharField(max_length = 30)
		
class Solicitacao(models.Model):
	id = models.AutoField(primary_key=True)
	texto = models.ForeignKey(Texto)
	usuario = models.ForeignKey(Usuario)
	tipo = models.CharField(max_length=1, choices=TIPO_SOLICITACAO_OPCOES)
	rodada = models.IntegerField()
	atendida = models.BooleanField()
	
	class Meta:
		db_table = 'Solicitacao'	