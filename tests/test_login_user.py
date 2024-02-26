import requests
import pytest
import random
import allure
from constants import Constants
from faker import Faker

faker = Faker()


class TestLoginUser:
    @allure.title('Авторизация под существующим пользователем')
    def test_login_with_correct_email_and_password(self, prepare_user):
        user = {
            "email": "julsus@yandex.ru",
            "password": "sus1992"
        }
        response = requests.post(Constants.url_login, data=user)

        assert 200 == response.status_code and '"success":true' in response.text

    @allure.title('Авторизация с неверным email')
    @pytest.mark.parametrize('email', [faker.email(), ''])
    def test_login_with_incorrect_email(self, prepare_user, email):
        user = {
            "email": email,
            "password": "sus1992"
        }
        response = requests.post(Constants.url_login, data=user)
        message = '{"success":false,"message":"email or password are incorrect"}'

        assert 401 == response.status_code and message in response.text

    @allure.title('Авторизация с неверным паролем')
    @pytest.mark.parametrize('password', [f"{random.randint(100000, 1000000)}", ''])
    def test_login_with_incorrect_password(self, prepare_user, password):
        user = {
            "email": "julsus@yandex.ru",
            "password": password
        }
        response = requests.post(Constants.url_login, data=user)
        message = '{"success":false,"message":"email or password are incorrect"}'

        assert 401 == response.status_code and message in response.text
