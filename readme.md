# Comandos para iniciar o projeto

#### Crie um ambiente virtual
``python -m venv nome_aqui``

#### Ativar o ambiente virtual
``.\nome_aqui\Scripts\Activate``

#### Sair do ambiente virtual
``deactivate``

#### Instale o Django
``pip install django``

#### Iniciar o projeto Django
``django-admin startproject nome_do_projeto``

#### Verifique o que está instalado no ambiente
``pip freeze``

#### Polls para criar o views
``python manage.py startapp polls``

#### Rodar as migrate
``python manage.py migrate``

#### Criar nova magration
``python manage.py makemigrations nome_aqui``

#### Rodar o servidor
``python manage.py runserver``

#### Criando super user
``python manage.py createsuperuser``

#### Criando requirements
``pip freeze > requirements.txt``


## Como funciona cada coisa do django

### URLs do django
Urls do django recebe 3 parâmetros 2 delas são obrigatórios
o 1 parâmetro é o url, 2 parâmetro é view e o 3 parâmetros é name

- url: recebe o rota
- view: recebe a função que vai ser executada na url
- name: é um apelido que damos para path para ser chamada em outros lugares

### Views do django
Views do django, views tem 2 passo para serem seguidos a 1 é request toda a view tem um request receber o argumento da rota que a chamou pode ser get ou post.
O 2 passo é sempre retornar algo o django não sabe o que fazer se não direcionamos ele o que retornar.


### Extensão de Templates
Templates tag no django para podemos editar parte em varios contexto
tag que usamos é block sua estrutura é 
``<title>{% block title%}{% endblock %}</title>``
``<body>{% block content%}{% endblock %}</body>``
block recebe um name e demos como title assim ele receber de qualquer página o title definido nele.
Para fazer que dados de outro página encorpora base usa-se a tag ``{% extends 'base.html' %}``
e nessa página que extende a base.html abrimos no arquivo 
``{% block title %}Seu título aqui{% endblock %}``
``{% block content %}<h1>Seu conteúdo html aqui</h1>{% endblock %}``

### Arquivos estáticos
Para usar arquivos estáticos no django usa-se tag load
``{% load static %}`` para usar siga esse padrão 
``<link rel="stylesheet" href="{% static 'css/styles.css' %}">`` como no exemplo depois da tag static colocamos o caminho do arquivo inserido.