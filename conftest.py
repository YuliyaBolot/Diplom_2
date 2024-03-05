import requests
import pytest
from constants import Urls
from constants import Data


@pytest.fixture(scope='function')
def prepare_user():
    user = Data.data_register
    response = requests.post(Urls.url_create_user, data=user)
    token = response.json()["accessToken"]
    yield prepare_user
    requests.delete(Urls.url_user, headers={'Authorization': token})

