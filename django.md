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

Abra o navegador nesse link:

http://127.0.0.1:8000/


# Fazer Migrações:


python myproject/manage.py makemigrations
python myproject/manage.py migrate 

python manage.py makemigrations
python manage.py migrate 

# Criar novo app:

cd myproject
python manage.py startapp novoapp


Para desativar o servidor: control + c
