from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, PostgresDsn, SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Bot(BaseModel):
    token: SecretStr


class Postgres(BaseModel):
    dsn: PostgresDsn


class Nats(BaseModel):
    dsn: str


class ApplicationSettings(BaseSettings):
    bot: Bot
    postgres: Postgres
    nats: Nats

    project_dir: Path = Field(Path(__file__).parent.parent.parent.parent.resolve(), const=True)

    model_config = SettingsConfigDict(env_file=project_dir / ".env", env_nested_delimiter="_")
