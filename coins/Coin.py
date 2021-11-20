import enum


class Coin(enum.Enum):
    ten_cents = 10
    twenty_cents = 20
    fifty_cents = 50
    hundred_cents = 100 # I assume this is what you meant with 1$,
    # cuz the 1$ is not a coin but you mentioned it in the CoinSlot section :)
    value = None

    # def __init__(self, value):
    #     self.value = value

    # def get_value(self) -> int:
    #     return self.value

