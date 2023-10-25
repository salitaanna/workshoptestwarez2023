import logging
import pytest
from pydantic_settings import BaseSettings, SettingsConfigDict

LOG_FILTERS = ["faker.factory", "urlib3.connectionpool"]


def pytest_configure():
    for logger_name in LOG_FILTERS:
        logger = logging.getLogger(logger_name)
        logger.disabled = True


class AdminAuth(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        env_prefix="QA_"
    )

    username: str
    password: str


@pytest.fixture
def admin_auth() -> AdminAuth:
    return AdminAuth()


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
        env_prefix="QA_"
    )

    base_url: str


@pytest.fixture
def env_settings() -> EnvSettings:
    return EnvSettings()

