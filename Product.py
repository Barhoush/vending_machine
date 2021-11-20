class Product:
    Snack_XL = (1, 3)  # My favorite drink :)
    Snack_REDBULL = (2, 6)
    Snack_KINDER = (3, 5)
    Snack_WATER = (4, 1)
    Snack_BURGER = (5, 50)

    number: int = None
    price: int = None

    def __init__(self, number: int, price: int):
        self.number = number
        self.price = price

    def get_number(self) -> int:
        return self.number

    def get_price(self) -> int:
        return self.price

    @staticmethod
    def get_product(selection) -> int:
        # Map the selected number from user with an actual product
        result = [product for key, product in Product.__dict__.items() if
               not key.startswith('__') and not callable(key) and key.startswith('Snack_')
                  and selection is product[0]]

        return result[0][0] if len(result) else None

    @staticmethod
    def get_product_obj(selection) -> any:
        # Map the selected number from user with an actual product
        result = [product for key, product in Product.__dict__.items() if
               not key.startswith('__') and not callable(key) and key.startswith('Snack_')
                  and selection is product[0]]

        return result[0] if len(result) else None
