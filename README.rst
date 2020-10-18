========
WebPrint
========

Compartilhador de imagens escrito em `django <https://www.djangoproject.com/>`_.

Ambiente de Desenvolvimento
===========================

- Crie uma cópia do `.env.example` para `.env`, e faça sua configuração:

  .. code-block:: sh

     cp .env.example .env

- Crie o ambiente com o `poetry <https://python-poetry.org/>`_:

  .. code-block:: sh

     poetry install

- Execute as migrações do banco de dados:

  .. code-block:: sh

     poetry run honcho run ./manage.py migrate

- Execute o servidor de desenvolvimento:

  .. code-block:: sh

     poetry run honcho run ./manage.py runserver

Docker
======

- Crie uma cópia do `.env.docker.example` para `.env.docker`, e faça sua configuração:

  .. code-block:: sh

     cp .env.docker.example .env.docker

- Execute as migrações do banco de dados:

  .. code-block:: sh

     docker-compose --env-file .env.docker run backend ./manage.py migrate

- Execute os conteiners:

  .. code-block:: sh

     docker-compose --env-file .env.docker up
