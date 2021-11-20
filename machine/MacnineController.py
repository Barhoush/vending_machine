from Product import Product
from calculator.MachineCalculator import MachineCalculator
from machine.Controller import Controller
from machine.Request import Request


class MachineController(Controller):
    calculator = MachineCalculator()

    def calculate_change(self, request: Request):
        total = self.calculator.calculate_total(request.entered_coins)
        change = total - request.product.get_price()
        return self.calculator.calculate_change(change)

