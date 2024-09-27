# Documentação Básica do Django

## Inicializando Servidor Local

Inicialize o ambiente virtual:

source myenv/bin/activate

Inicialize o servidor:

python myproject/manage.py runserver

Abra o navegador nesse link:

http://127.0.0.1:8000/

Para desativar o servidor: control + c

# Fazer Migrações:


python myproject/manage.py makemigrations
python myproject/manage.py migrate 

# Criar novo app:

python myproject/manage.py startapp novoapp


