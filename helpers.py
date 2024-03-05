import requests
import allure
from constants import Data
from constants import Urls


class Helpers:

    @allure.step('Получаем токен залогиненного пользователя')
    def get_user_token(self):
        user = Data.data_login
        response_post = requests.post(Urls.url_login, data=user)
        token = response_post.json()["accessToken"]
        return token

    @allure.step('Создаем заказ из ингредиентов')
    def create_order(self):
        response_ingredients = requests.get(Urls.url_ingredients)
        ingredient_1 = response_ingredients.json()["data"][0]["_id"]
        ingredient_2 = response_ingredients.json()["data"][1]["_id"]
        order = {
            "ingredients": [ingredient_1, ingredient_2]
        }
        return order
