###################
Awesome Application
###################

Запуск
======

Заполни ``.env.dist``, затем -> ``.env``

.. code-block:: shell

    poetry install
    alembic upgrade head
    python -m src.awesome

.. code-block:: shell

    taskiq worker awesome.services.notify:broker

.. code-block:: shell

    taskiq scheduler awesome.services.notify:scheduler

