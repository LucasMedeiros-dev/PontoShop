from .serializers import PresencaSerializer, ImersionistaSerializer, TipoUserSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from project.CustomPermissions import IsInstrutorOrMonitor, ImersionistaReadOnly
from .models import UserActivityLogger
from ponto.models import Presenca, Imersionista
from django.utils import timezone


class ImersionistaViewSet(ReadOnlyModelViewSet):
    serializer_class = ImersionistaSerializer
    permission_classes = [ImersionistaReadOnly]

    def get_queryset(self):
        return Imersionista.objects.filter(turma__responsavel__user=self.request.user)


class PresencaViewSet(ModelViewSet):
    serializer_class = PresencaSerializer
    permission_classes = [IsInstrutorOrMonitor]

    def get_queryset(self):
        return Presenca.objects.filter(
            aluno__turma__responsavel__user=self.request.user
        )

    def create(self, request, *args, **kwargs):
        # Apenas registre a presença se o usuário for o responsável pela turma do aluno
        UserActivityLogger.objects.create(
            evento=f"Presença de {request.data['aluno']} no dia {request.data['data']} registrada",
            data=timezone.now(),
            usuario=request.user.username,
        )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        presenca = self.get_object()
        # Apenas registre a presença se o usuário for o responsável pela turma do aluno

        UserActivityLogger.objects.create(
            evento=f"Presença de {presenca.aluno.nome} no dia {presenca.data} alterada",
            data=timezone.now(),
            usuario=request.user.username,
        )

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        presenca = self.get_object()
        # Apenas registre a presença se o usuário for o responsável pela turma do aluno

        UserActivityLogger.objects.create(
            evento=f"Presença de {presenca.aluno.nome} no dia {presenca.data} alterada",
            data=timezone.now(),
            usuario=request.user.username,
        )
        return super().partial_update(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TipoUserSerializer
