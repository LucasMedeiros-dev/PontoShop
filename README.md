# PontoShop - Gerenciamento de Presenças no Workshop de Imersão da Fábrica de Software 2024.2

Este é um projeto Django para gerenciar presenças e imersionistas.

## Requisitos

- Python 3.11
- Django 5.1
- Django REST Framework
- Django Simple JWT

## Configuração do Ambiente

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/ponto.git
    cd ponto
    ```

2. Crie e ative um ambiente virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```sh
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin do Django:

    ```sh
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

## Endpoints

### Autenticação

- `POST /login/` - Obter token de autenticação
- `POST /login/refresh/` - Atualizar token de autenticação

### Admin

- `GET /admin/` - Acesso ao painel administrativo do Django

### API

- `GET /api/imersionistas/` - Listar imersionistas
- `GET /api/imersionistas/{id}/` - Detalhar um imersionista
- `GET /api/presencas/` - Listar presenças
- `GET /api/presencas/{id}/` - Detalhar uma presença

## Estrutura do Projeto

- `manage.py` - Script de gerenciamento do Django
- `ponto/` - Aplicação principal
  - `models.py` - Modelos do banco de dados
  - `views.py` - Views da aplicação
  - `serializers.py` - Serializadores da API
  - `urls.py` - Rotas da aplicação
  - `tests.py` - Testes da aplicação
- `project/` - Configurações do projeto
  - `settings.py` - Configurações do Django
  - `urls.py` - Rotas principais do projeto
  - `wsgi.py` - Configuração WSGI para deploy

## Configurações Adicionais

### CORS

Para permitir origens específicas, edite o arquivo [project/settings.py](project/settings.py):

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
```

### JWT

As configurações do JWT estão no arquivo project/settings.py

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```