import pytest
from httpx import AsyncClient


@pytest.fixture
def app():
    from src.main import create_app
    app = create_app()
    yield app


@pytest.fixture
def client(event_loop, app):
    client = AsyncClient(app=app, base_url='http://test')
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest.fixture
def shipping_options():
    return [
        dict(name='Entrega Ninja',
             min_height=10,
             max_height=200,
             min_width=6,
             max_width=140,
             delivery_deadline=6),
        dict(name='Entrega KaBuM',
             min_height=5,
             max_height=140,
             min_width=13,
             max_width=125,
             delivery_deadline=4)
    ]
