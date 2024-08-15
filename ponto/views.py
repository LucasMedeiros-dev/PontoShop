from .serializers import PresencaSerializer, ImersionistaSerializer, TipoUserSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from project.CustomPermissions import IsInstrutorOrMonitor
from ponto.models import Presenca, Imersionista


class ImersionistaViewSet(ReadOnlyModelViewSet):
    serializer_class = ImersionistaSerializer
    permission_classes = [IsInstrutorOrMonitor]

    def get_queryset(self):
        return Imersionista.objects.filter(turma__responsavel__user=self.request.user)


class PresencaViewSet(ModelViewSet):
    serializer_class = PresencaSerializer
    permission_classes = [IsInstrutorOrMonitor]

    def get_queryset(self):
        return Presenca.objects.filter(
            aluno__turma__responsavel__user=self.request.user
        )


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TipoUserSerializer
