from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Bot(BaseModel):
    token: SecretStr


class PostgreSQL(BaseModel):
    dsn: PostgresDsn


class Nats(BaseModel):
    dsn: str


class Settings(BaseSettings):
    bot: Bot
    postgres: PostgreSQL
    nats: Nats

    project_dir: ClassVar[Path] = Path(__file__).parent.parent.parent.parent.resolve()

    model_config = SettingsConfigDict(env_file=project_dir / ".env", env_nested_delimiter="_")
