import requests
from models import Item


class Parse:
    def __init__(self, id_item: str):
        self.id_item = id_item

    def parse(self) -> Item:
        params = {
            'dest': '-1257786',
            'nm': self.id_item,
        }
        response = requests.get('https://card.wb.ru/cards/v2/detail', params=params)
        return self.__get_item_data(response.json()["data"]["products"][0])

    def __get_item_data(self, response: dict):
        item_data = {
            "id": self.id_item,
            "brand": response["brand"],
            "name": response["name"],
            "rating": response["reviewRating"],
            "feedbacks": response["feedbacks"],
            "volume": response["volume"],
            "price": response["sizes"][0]["price"]["product"]
        }
        return self.__create_item_obj(item_data)

    def __create_item_obj(self, item_data: dict):
        item_obj = Item.parse_obj(item_data)
        print(item_obj)
        print(type(item_obj))
        return item_obj


if __name__ == "__main__":
    Parse("17902726").parse()