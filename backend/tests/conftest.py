import os
from pathlib import Path
from urllib.parse import unquote, urlparse

import psycopg
import pytest
from dotenv import load_dotenv

test_env = Path(__file__).resolve().parent.parent / ".env.test"

load_dotenv(test_env, override=True)


@pytest.fixture(scope="session", autouse=True)
def require_test_database():
    database_url = os.environ.get("DATABASE_URL")
    assert database_url, "DATABASE_URL must be set by .env.test"

    database_name = unquote(urlparse(database_url).path).lstrip("/")
    assert database_name == "career_profiles_test", (
        "Tests must use the career_profiles_test database, not another database"
    )

    with psycopg.connect(database_url) as connection:
        connected_database = connection.execute(
            "SELECT current_database()"
        ).fetchone()[0]
    assert connected_database == "career_profiles_test", (
        "PostgreSQL connection did not reach the career_profiles_test database"
    )