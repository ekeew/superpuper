from pydantic import BaseModel, BaseSettings, SecretStr, PostgresDsn


class Bot(BaseModel):
    token: SecretStr


class Postgres(BaseModel):
    dsn: PostgresDsn


class Settings(BaseSettings):
    bot: Bot
    postgres: Postgres

    class Config:
        env_file = ".env"
        env_nested_delimiter = "_"
