class Urls:

    url_create_user = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    url_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    url_ingredients = 'https://stellarburgers.nomoreparties.site/api/ingredients'
    url_order = 'https://stellarburgers.nomoreparties.site/api/orders'
    url_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'


class Data:

    data_register = {
        "email": "julsus@yandex.ru",
        "password": "sus1992",
        "name": "Yuliya"
    }

    data_login = {
            "email": "julsus@yandex.ru",
            "password": "sus1992"
    }

    user_data = [{
            "email": "",
            "password": "sus1992",
            "name": "Yuliya"
    },
        {
            "email": "julsus@yandex.ru",
            "password": "",
            "name": "Yuliya"
    },
        {
            "email": "julsus@yandex.ru",
            "password": "sus1992",
            "name": ""
    }
    ]
