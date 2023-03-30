import pytest

from src.app import create_app


@pytest.fixture
def flask_app():
    yield create_app()


@pytest.fixture
def flask_client(flask_app):
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client
