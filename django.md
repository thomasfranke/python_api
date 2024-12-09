# Documentação Básica do Django

## Inicializando Servidor Local

Criar o ambiente:

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt


- Instalar dependencias pelo Requirements:

- Instalar dependencias de forma Manual:
pip install django
pip install djangorestframework django-cors-headers django-extensions
pip install drf_spectacular
pip install djangorestframework-simplejwt
python -m pip install Pillow


Inicialize o ambiente virtual:

source env/bin/activate

Inicialize o servidor:

python myproject/manage.py makemigrations
python myproject/manage.py migrate 
python myproject/manage.py runserver
python manage.py runserver

Abra o navegador nesse link:

http://127.0.0.1:8000/

# Reset Migrations:
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete


# Fazer Migrações:

- Se não estiver criando a tabela:
python manage.py makemigrations perfil --empty
python manage.py makemigrations <tabela> --empty

python myproject/manage.py makemigrations
python myproject/manage.py migrate 

python manage.py makemigrations
python manage.py migrate 

# Criar novo app:

cd myproject
python manage.py startapp novoapp


Para desativar o servidor: control + c
