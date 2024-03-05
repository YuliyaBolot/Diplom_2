import requests
import allure
import random
import string
import pytest
from constants import Urls
from helpers import Helpers


class TestCreateOrder:
    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_with_authorization(self, prepare_user):
        helper = Helpers()
        token = helper.get_user_token()
        order = helper.create_order()
        response = requests.post(Urls.url_order, headers={'Authorization': token}, data=order)

        assert 200 == response.status_code and '"success":true' in response.text

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self, prepare_user):
        helper = Helpers()
        order = helper.create_order()
        response = requests.post(Urls.url_order, data=order)

        assert 200 == response.status_code and '"success":true' in response.text

    @allure.title('Создание заказа с указанием ингредиентов')
    def test_create_order_with_ingredients(self, prepare_user):
        helper = Helpers()
        token = helper.get_user_token()
        response_ingredients = requests.get(Urls.url_ingredients)
        ingredient_1 = response_ingredients.json()["data"][2]["_id"]
        ingredient_2 = response_ingredients.json()["data"][6]["_id"]
        ingredient_3 = response_ingredients.json()["data"][8]["_id"]
        order = {
            "ingredients": [ingredient_1, ingredient_2, ingredient_3]
        }
        response = requests.post(Urls.url_order, headers={'Authorization': token}, data=order)
        order_details = response.json()["order"]["status"]

        assert 200 == response.status_code and order_details == "done"

    @allure.title('Создание заказа без указания ингредиентов')
    def test_try_create_order_without_ingredients(self, prepare_user):
        helper = Helpers()
        token = helper.get_user_token()
        response = requests.post(Urls.url_order, headers={'Authorization': token})
        message = '{"success":false,"message":"Ingredient ids must be provided"}'

        assert 400 == response.status_code and message in response.text

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    @pytest.mark.parametrize('ingredient', [random.randint(0, 1000000),
                                            ''.join(random.choice(string.ascii_lowercase) for i in range(1000))])
    def test_try_create_order_with_invalid_ingredients(self, prepare_user, ingredient):
        helper = Helpers()
        token = helper.get_user_token()
        order = {"ingredients": ingredient}
        response = requests.post(Urls.url_order, headers={'Authorization': token}, data=order)

        assert 500 == response.status_code








