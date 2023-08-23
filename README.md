Awesome Bot [от тостера]
===

### Запуск

Заполни `.env.dist`, затем -> `.env`

```shell
poetry install
poetry run alembic upgrade head
poetry run python -m awesome.telegram
```
```shell
poetry run taskiq worker awesome.core.services.notify:broker
```
```shell
poetry run taskiq scheduler awesome.core.services.notify:scheduler
```
