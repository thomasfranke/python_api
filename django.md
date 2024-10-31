# Documentação Básica do Django

## Inicializando Servidor Local

Inicialize o ambiente virtual:

source myenv/bin/activate

Inicialize o servidor:

python myproject/manage.py runserver

Abra o navegador nesse link:

http://127.0.0.1:8000/

## Autenticacao:

POST: http://127.0.0.1:8000/autenticacao/autenticar/
Body: {
    "username": "thomas1",
    "password": "123456"
}


Para desativar o servidor: control + c

# Fazer Migrações:


python myproject/manage.py makemigrations
python myproject/manage.py migrate 

# Criar novo app:

cd myproject
python manage.py startapp novoapp


Para desativar o servidor: control + c
