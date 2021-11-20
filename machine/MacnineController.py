from Product import Product
from calculator.MachineCalculator import MachineCalculator
from machine.Controller import Controller
from machine.Request import Request


class MachineController(Controller):
    calculator = MachineCalculator()

    def calculate_change(self, request: Request):
        print("request.entered_coins", request.entered_coins)
        total = self.calculator.calculate_total(request.entered_coins)
        print("request.product.get_price()", request.product.get_price())
        print("total", total)
        change = total - request.product.get_price()
        return self.calculator.calculate_change(change)

