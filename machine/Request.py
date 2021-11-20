from Product import Product
from coins.CoinGroup import CoinGroup


class Request:
    product: Product = None
    entered_coins: CoinGroup = None

    def __init__(self, selected_products: int, entered_coins: list, product: Product = None):
        self.product = product if product else Product.get_product(selection=selected_products)
        if self.product is None:
            print("Log: product is none!")
        self.entered_coins = CoinGroup(entered_coins)
