from pydantic import BaseModel, BaseSettings, SecretStr, PostgresDsn


class Bot(BaseModel):
    token: SecretStr


class Postgres(BaseModel):
    dsn: PostgresDsn


class Nats(BaseModel):
    dsn: str


class Settings(BaseSettings):
    bot: Bot
    postgres: Postgres
    nats: Nats

    class Config:
        env_file = ".env"
        env_nested_delimiter = "_"
