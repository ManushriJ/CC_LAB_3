import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    all_products = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail["contents"])
        except json.JSONDecodeError:
            continue  # Skip invalid JSON contents
        all_products.extend(products.get_product(item) for item in contents)
    
    return all_products

    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


