from django.contrib import admin

# Register your models here.
from editor.models import Usuario
admin.site.register(Usuario)

from editor.models import Genero
admin.site.register(Genero)

from editor.models import Texto
admin.site.register(Texto)

from editor.models import Texto_Usuario
admin.site.register(Texto_Usuario)

from editor.models import Paragrafo
admin.site.register(Paragrafo)

from editor.models import Solicitacao
admin.site.register(Solicitacao)