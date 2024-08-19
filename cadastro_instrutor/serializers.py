from rest_framework import serializers
from ponto.models import Responsavel


class UsuarioCreateSerializers(serializers.Serializer):
    email = serializers.EmailField()
    cargo = serializers.ChoiceField(choices=Responsavel.Cargo.choices)
