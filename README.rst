###################
Awesome Application
###################

Запуск
======

Заполни ``.env.dist``, затем -> ``.env``

.. code-block:: shell

    poetry install
    alembic upgrade head

.. code-block:: shell

    python -m src.awesome.presentation.bot

.. code-block:: shell

    python -m src.awesome.presentation.services

.. code-block:: shell

    taskiq worker awesome.services.notify:broker

.. code-block:: shell

    taskiq scheduler awesome.services.notify:scheduler

