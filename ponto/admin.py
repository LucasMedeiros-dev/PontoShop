from django.contrib import admin
from .models import Responsavel, Turma, Imersionista, Presenca, UserActivityLogger
# Register your models here.


@admin.register(UserActivityLogger)
class UserActivityLoggerAdmin(admin.ModelAdmin):
    list_display = ("data", "evento", "usuario")
    list_filter = ("data", "usuario")
    search_fields = ("evento", "usuario")


admin.site.register(Responsavel)

admin.site.register(Turma)

admin.site.register(Imersionista)


@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ("aluno", "data", "situacao", "aluno__turma")
    list_filter = ("aluno__turma__nome", "data", "situacao")
    search_fields = ("aluno", "rgm")
