# Documentação Básica do Django

## Inicializando Servidor Local

Inicialize o ambiente virtual:

source env/bin/activate

Inicialize o servidor:

python myproject/manage.py runserver

Abra o navegador nesse link:

http://127.0.0.1:8000/


# Fazer Migrações:


python myproject/manage.py makemigrations
python myproject/manage.py migrate 

# Criar novo app:

cd myproject
python manage.py startapp novoapp


Para desativar o servidor: control + c
