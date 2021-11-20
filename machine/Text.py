from Product import Product
from machine.MacnineController import MachineController
from machine.Request import Request
from machine.VendingMachine import VendingMachine
from coins.CoinGroup import CoinGroup


class Text(VendingMachine):
    controller: MachineController = MachineController()
    selected_product: int = None
    change: CoinGroup = None

    def display_items(self) -> None:
        """Overrides VendingMachine.display_items()"""
        print(f"Welcome to the best Vending Machine in Ramallah! We have these cool products served with love: ")
        print({key: value for key, value in Product.__dict__.items() if
               not key.startswith('__') and key.startswith('Snack_') and not callable(key)})

    def select_item(self, item_no: int) -> bool:
        available_items = [value[0] for key, value in Product.__dict__.items() if
                           not key.startswith('__') and key.startswith('Snack_') and not callable(key)]

        if item_no not in available_items:
            return False
        self.selected_product = item_no
        return True

    def display_message(self, message: str) -> None:
        print(f"Please enter coins at each denominations at the following order: ")
        print(f"#of 10cents, #of 20cents, #of 50cents, #of 100cents")
        print(f"Example: 3 10cents would be (3,0,0,0)")

    def enter_coins(self, coins: list) -> None:
        product_pairs = Product.get_product_obj(self.selected_product)
        product = Product(product_pairs[0], product_pairs[1])
        request = Request(self.selected_product, coins, product)
        # change = CoinGroup(coins=coins)
        change = self.controller.calculate_change(request=request)
        self.change = change

    def display_change_message(self, message: str) -> None:
        print(f"Your returned change: ")
        print(f"10cents {self.change.number_10_coin}")
        print(f"20cents {self.change.number_20_coin}")
        print(f"50cents {self.change.number_50_coin}")
        print(f"100cents {self.change.number_100_coin}")
