from django.contrib import admin
from .models import Responsavel, Turma, Imersionista, Presenca
# Register your models here.

admin.site.register(Responsavel)

admin.site.register(Turma)

admin.site.register(Imersionista)


@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ("aluno", "data", "situacao", "aluno__turma")
    list_filter = ("aluno__turma__nome", "data", "situacao")
    search_fields = ("aluno", "rgm")
