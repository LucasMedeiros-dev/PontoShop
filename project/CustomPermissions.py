from rest_framework import permissions
from ponto.models import Responsavel


class IsInstrutorOrMonitor(permissions.BasePermission):
    """
    Permissão customizada para permitir que Instrutores tenham todas as permissões,
    enquanto Monitores só podem visualizar e criar.
    """

    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado
        if not request.user or not request.user.is_authenticated:
            return False

        # Verifica se o usuário tem um perfil de Responsável
        try:
            responsavel = request.user.responsavel
        except Responsavel.DoesNotExist:
            return False

        # Instrutores têm todas as permissões
        if responsavel.cargo == Responsavel.Cargo.INSTRUTOR:
            return True

        # Monitores podem apenas visualizar (GET, HEAD, OPTIONS) e criar (POST)
        if responsavel.cargo == Responsavel.Cargo.MONITOR:
            if request.method in permissions.SAFE_METHODS or request.method == "POST":
                return True

        # Caso contrário, negar permissão
        return False
