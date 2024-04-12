from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_VERSION: str = "1.0.0"
    CONTACT: dict = {"name": "yejunyu", "email": "", "url": ""}
    ENV: str = "dev"
    if ENV == "dev":
        RELOAD: bool = True
        LOG_LEVEL: str = "DEBUG"
    else:
        RELOAD: bool = False
        LOG_LEVEL: str = "INFO"
    ALLOWED_HOSTS: list = ["*"]

    MYSQL_HOST: str = "117.72.37.213"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "Bb1387205?"
    MYSQL_PORT: int = 3307
    MYSQL_DB: str = "todolist"

    class Config:
        env_file = "./.env"
        extra = "ignore"


settings = Settings()
