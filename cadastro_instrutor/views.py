from .serializers import UsuarioCreateSerializers
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from ponto.models import Responsavel
from rest_framework import status


# Create your views here.


message = Mail(
    from_email="lucasm676@gmail.com",
    to_emails="lucasm676@gmail.com",
    subject="Login no Sistema FABPonto",
    html_content="""Olá [Nome do Usuário],

É com grande alegria que informamos que você foi escolhido para a função de [Nome da Função]! Parabéns por essa conquista!

Estamos confiantes de que suas habilidades e experiência serão de grande valor para nossa equipe, e estamos animados para ver o impacto positivo que você trará.

Para começar a usar o nosso sistema, você pode acessar o aplicativo através do link abaixo:

Link do App: [Insira o link aqui]

Aqui estão suas credenciais de acesso:

Login: [Insira o login do usuário aqui]
Senha: [Insira a senha do usuário aqui]

Por favor, ao fazer o primeiro login, recomendamos que você altere sua senha para garantir a segurança da sua conta.

Se precisar de qualquer assistência ou tiver dúvidas, sinta-se à vontade para entrar em contato com nossa equipe de suporte.

Mais uma vez, parabéns! Estamos ansiosos para trabalhar com você nessa nova fase.

Atenciosamente,

[Seu Nome]
[Seu Cargo]
[Nome da Empresa]""",
)
try:
    sg = SendGridAPIClient("Change")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)


class CreateUsersViewSet(ViewSet):
    def create(self, request):
        serializer = UsuarioCreateSerializers(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data["email"],
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            responsavel = Responsavel.objects.create(
                user=user, cargo=serializer.validated_data["cargo"]
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
