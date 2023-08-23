###################
Awesome Application
###################

Запуск
======

Заполни ``.env.dist``, затем -> ``.env``

.. code-block:: shell

    poetry install
    poetry run alembic upgrade head
    poetry run python -m src.awesome

.. code-block:: shell

    poetry run taskiq worker awesome.services.notify:broker

.. code-block:: shell

    poetry run taskiq scheduler awesome.services.notify:scheduler

