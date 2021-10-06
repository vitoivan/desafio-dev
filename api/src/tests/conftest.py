import pytest
from src import create_app

@pytest.fixture(scope='module')
def app():
    """Instance of main flask app per python module"""
    return create_app()