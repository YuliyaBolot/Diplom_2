import requests
import allure
from constants import Urls
from helpers import Helpers


class TestUserOrder:
    @allure.title('Получение заказа авторизованного пользователя')
    def test_get_authorization_user_order(self, prepare_user):
        helper = Helpers()
        token = helper.get_user_token()
        order = helper.create_order()
        requests.post(Urls.url_order, headers={'Authorization': token}, data=order)
        response_get = requests.get(Urls.url_order, headers={'Authorization': token})

        assert 200 == response_get.status_code and '"success":true' in response_get.text

    @allure.title('Попытка получения заказа неавторизованного пользователя')
    def test_user_order_without_authorization(self):
        response_get = requests.get(Urls.url_order)
        message = '{"success":false,"message":"You should be authorised"}'

        assert 401 == response_get.status_code and message in response_get.text


