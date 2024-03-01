import requests
import allure
import pytest
import random
from constants import Data
from constants import Urls
from faker import Faker

faker = Faker()


class TestCreateUser:


    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self):
        user = {
            "email": faker.email(),
            "password": f"{random.randint(100000, 1000000)}",
            "name": faker.name()
        }
        response = requests.post(Urls.url_create_user, data=user)
        assert 200 == response.status_code and '"success":true' in response.text

    @allure.title('Попытка создать пользователя, который уже зарегистрирован')
    def test_try_create_user_which_already_exists(self, prepare_user):
        user = Data.data_register
        response = requests.post(Urls.url_create_user, data=user)
        message = '{"success":false,"message":"User already exists"}'

        assert 403 == response.status_code and message in response.text

    @allure.title('Попытка создать пользователя, без заполнения одного из обязательных полей')
    @pytest.mark.parametrize('user_data', Data.user_data)
    def test_try_create_user_without_one_required_field(self, user_data):
        user = user_data
        response = requests.post(Urls.url_create_user, data=user)
        message = '{"success":false,"message":"Email, password and name are required fields"}'

        assert 403 == response.status_code and message in response.text

