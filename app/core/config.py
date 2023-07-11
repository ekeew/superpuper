from pydantic import BaseModel, BaseSettings, SecretStr, PostgresDsn, Field


class Bot(BaseModel):
    token: SecretStr


class Postgres(BaseModel):
    dsn: PostgresDsn


class Nats(BaseModel):
    dsn: str  # So sad.....


class Settings(BaseSettings):
    bot: Bot
    postgres: Postgres
    nats: Nats
    admin_ids_raw: str = Field(env="admin_ids")

    @property
    def admin_ids(self) -> tuple:
        return tuple(map(int, self.admin_ids_raw.split(",")))

    class Config:
        env_file = ".env"
        env_nested_delimiter = "_"
