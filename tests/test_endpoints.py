import pytest
import requests
from flaskr import create_app


@pytest.fixture()
def app():
    app = create_app(test_config=True)

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_arrets(client):
    response = client.get("/arrets")
    assert response.status_code == 200
