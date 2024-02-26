import requests
import pytest
from constants import Constants

@pytest.fixture(scope='function')
def prepare_user():
    user = {
        "email": "julsus@yandex.ru",
        "password": "sus1992",
        "name": "Yuliya"
    }
    response = requests.post(Constants.url_create_user, data=user)
    token = response.json()["accessToken"]
    yield prepare_user
    requests.delete(Constants.url_user, headers={'Authorization': token})

