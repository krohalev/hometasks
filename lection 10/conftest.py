import pytest
from datetime import datetime

@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print(f'Тесты запущены в {datetime.now()} ')

    yield

    print(f'\nТесты закончены в {datetime.now()} ')


@pytest.fixture(scope='function')
def test_fixture():
    print('тут')