import requests
from constants import Constants


class Helpers:

    def get_user_token(self):
        user = {
            "email": "julsus@yandex.ru",
            "password": "sus1992"
        }
        response_post = requests.post(Constants.url_login, data=user)
        token = response_post.json()["accessToken"]
        return token

    def create_order(self):
        response_ingredients = requests.get(Constants.url_ingredients)
        ingredient_1 = response_ingredients.json()["data"][0]["_id"]
        ingredient_2 = response_ingredients.json()["data"][1]["_id"]
        order = {
            "ingredients": [ingredient_1, ingredient_2]
        }
        return order
