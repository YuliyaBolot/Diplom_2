import requests
import pytest
import allure
from constants import Urls
from helpers import Helpers


class TestChangeUserData:

    @allure.title('Изменение имени авторизованного пользователя')
    def test_change_user_name(self, prepare_user):
        helper = Helpers()
        token = helper.get_user_token()
        user_change = {"name": "Juliya"}
        response_patch = requests.patch(Urls.url_user, headers={'Authorization': token}, data=user_change)
        message = '{"success":true,"user":{"email":"julsus@yandex.ru","name":"Juliya"}}'

        assert 200 == response_patch.status_code and message in response_patch.text

    @allure.title('Изменение email авторизованного пользователя')
    def test_change_user_email(self, prepare_user):
        helper = Helpers()
        token = helper.get_user_token()
        user_change = {"email": "julsus54@yandex.ru"}
        response_patch = requests.patch(Urls.url_user, headers={'Authorization': token}, data=user_change)
        message = '{"success":true,"user":{"email":"julsus54@yandex.ru","name":"Yuliya"}}'

        assert 200 == response_patch.status_code and message in response_patch.text

    @allure.title('Изменение пароля авторизованного пользователя')
    def test_change_user_password(self, prepare_user):
        helper = Helpers()
        token = helper.get_user_token()
        user_change = {"password": "suslova1992"}
        response_patch = requests.patch(Urls.url_user, headers={'Authorization': token}, data=user_change)
        message = '{"success":true,"user":{"email":"julsus@yandex.ru","name":"Yuliya"}}'

        assert 200 == response_patch.status_code and message in response_patch.text

    @allure.title('Попытка изменить данные пользователя без авторизации')
    @pytest.mark.parametrize('data_change', [{"name": "Juliya"}, {"email": "julsus54@yandex.ru"}, {"password": "suslova1992"}])
    def test_try_change_user_data_without_authorization(self, prepare_user, data_change):
        user_change = data_change
        response = requests.patch(Urls.url_user, data=user_change)
        message = '{"success":false,"message":"You should be authorised"}'

        assert 401 == response.status_code and message in response.text

