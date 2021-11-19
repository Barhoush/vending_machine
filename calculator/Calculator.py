from Helpers.MachineHelper import MachineHelper
from coins.CoinGroup import CoinGroup


class Calculator(MachineHelper):
    def calculate_total(self, coins: CoinGroup) -> int:
        pass

    def calculate_change(self, entered_money: int) -> CoinGroup:
        pass
