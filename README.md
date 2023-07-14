Awesome Bot [от тостера]
===

### Запуск

Заполни `.env.dist`, затем -> `.env`

```shell
poetry install
poetry run alembic upgrade head
poetry run python -m app.bot
```
```shell
poetry run taskiq worker app.core.services.notify:broker
```
```shell
poetry run taskiq scheduler app.core.services.notify:scheduler
```
