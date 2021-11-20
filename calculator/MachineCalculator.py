from calculator.Calculator import Calculator
from coins.Coin import Coin
from coins.CoinGroup import CoinGroup


class MachineCalculator(Calculator):
    def calculate_total(self, coins: CoinGroup) -> int:
        return coins.get_total()

    def calculate_change(self, entered_money: int) -> CoinGroup:
        change: CoinGroup = CoinGroup()
        remaining_amount = entered_money
        change.number_100_coin = remaining_amount / Coin.hundred_cents.value
        remaining_amount = remaining_amount % Coin.hundred_cents.value

        change.number_50_coin = remaining_amount / Coin.fifty_cents.value
        remaining_amount = remaining_amount % Coin.fifty_cents.value

        change.number_20_coin = remaining_amount / Coin.twenty_cents.value
        remaining_amount = remaining_amount % Coin.twenty_cents.value

        change.number_10_coin = remaining_amount / Coin.ten_cents.value

        return change
