class Product:
    XL = (1, 3)  # My favorite drink :)
    RED_BULL = (2, 6)
    KINDER = (3, 5)
    WATER = (4, 1)
    BURGER = (5, 50)

    number: int = None
    price: int = None

    def __init__(self, number: int, price: int):
        self.number = number
        self.price = price

    def get_number(self) -> int:
        return self.number

    def get_price(self) -> int:
        return self.price

    def get_product(self, selection):
        # Map the selected number from user with an actual product
        result = [product for key, product in Product.__dict__.items() if
               not key.startswith('__') and not callable(key) and selection is product.get_number()]

        return result[0] if len(result) else None
