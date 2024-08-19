from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Create your views here.


message = Mail(
    from_email="lucasm676@gmail.com",
    to_emails="zweell13@gmail.com",
    subject="Login no Sistema FABPonto",
    html_content="""Olá [Nome do Usuário],<br><br>

É com grande alegria que informamos que você foi escolhido para a função de [Nome da Função]! Parabéns por essa conquista!<br><br>

A função do sistema é facilitar o controle de ponto dos imersionistas, permitindo que os monitores e instrutores possam visualizar e registrar a presença dos alunos.<br><br>

Para começar a usar o nosso sistema, você pode acessar o aplicativo através do link abaixo:<br><br>

Link do App: [Insira o link aqui]<br><br>

Aqui estão suas credenciais de acesso:<br><br>

Login: [Insira o login do usuário aqui]<br>
Senha: [Insira a senha do usuário aqui]<br><br>

Por favor, ao fazer o primeiro login, recomendamos que você altere sua senha para garantir a segurança da sua conta.<br><br>

Se precisar de qualquer assistência ou tiver dúvidas, sinta-se à vontade para entrar em contato com nossa equipe de suporte.<br><br>


Atenciosamente,

Lucas Medeiros,
Responsável por Back-End.
""",
)
try:
    sg = SendGridAPIClient("Change")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
