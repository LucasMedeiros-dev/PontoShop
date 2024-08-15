from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ponto.models import Presenca, Imersionista, Responsavel
from rest_framework.serializers import ModelSerializer


class ImersionistaSerializer(ModelSerializer):
    class Meta:
        model = Imersionista
        fields = "__all__"


class PresencaSerializer(ModelSerializer):
    class Meta:
        model = Presenca
        fields = "__all__"


class TipoUserSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Assuming the user is linked to a Responsavel
        try:
            responsavel = Responsavel.objects.get(user=self.user)
            data["cargo"] = responsavel.cargo
        except Responsavel.DoesNotExist:
            data["cargo"] = None  # Or handle as you see fit

        return data
