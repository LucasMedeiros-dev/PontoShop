from .serializers import UsuarioCreateSerializers
from django.utils.crypto import get_random_string
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from ponto.models import Responsavel
from rest_framework import status
from django.conf import settings


class CreateUsersViewSet(ViewSet):
    serializer_class = UsuarioCreateSerializers

    def create(self, request):
        serializer = UsuarioCreateSerializers(data=request.data)
        if serializer.is_valid():
            # Gera uma senha randômica
            password = get_random_string(length=12)

            # Cria o usuário
            user = User.objects.create_user(
                username=serializer.validated_data["email"],
                email=serializer.validated_data["email"],
                password=password,
            )
            responsavel = Responsavel.objects.create(
                user=user, cargo=serializer.validated_data["cargo"]
            )

            # Prepara o conteúdo do email
            email_content = f"""Olá Veterano!,<br><br>

            É com grande alegria que informamos que você foi escolhido para a função de {responsavel.get_cargo_display()}! Parabéns por essa conquista!<br><br>

            A função do sistema é facilitar o controle de ponto dos imersionistas, permitindo que os monitores e instrutores possam visualizar e registrar a presença dos alunos.<br><br>

            Para começar a usar o nosso sistema, você pode acessar o aplicativo através do link abaixo:<br><br>

            Link do App: <a href='https://linkdoapp.com'>https://linkdoapp.com</a><br><br>

            Aqui estão suas credenciais de acesso:<br><br>

            Login: {user.username}<br>
            Senha: {password}<br><br>

            Por favor, ao fazer o primeiro login, recomendamos que você altere sua senha para garantir a segurança da sua conta.<br><br>

            Se precisar de qualquer assistência ou tiver dúvidas, sinta-se à vontade para entrar em contato com nossa equipe de suporte.<br><br>

            Atenciosamente,<br><br>

            Lucas Medeiros,<br>
            Responsável por Back-End.
            """

            # Envia o email
            message = Mail(
                from_email="lucasm676@gmail.com",
                to_emails=user.email,
                subject="Login no Sistema FABPonto",
                html_content=email_content,
            )
            try:
                sg = SendGridAPIClient(settings.SG_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)
                return Response(
                    {"error": "Erro ao enviar o e-mail."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
