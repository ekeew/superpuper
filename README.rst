###################
Awesome Application
###################

Запуск
======

Заполни ``.env.dist``, затем -> ``.env``

.. code-block:: shell

    poetry install
    poetry run alembic upgrade head
    poetry run python -m awesome.telegram

.. code-block:: shell

    poetry run taskiq worker awesome.core.services.notify:broker

.. code-block:: shell

    poetry run taskiq scheduler awesome.core.services.notify:scheduler

