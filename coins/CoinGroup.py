class CoinGroup:
    # As we'll be continuously receiving a group of coins and returning it, let's stay more OOP geek and use classes
    # instead of lists

    number_10_coin = None
    number_20_coin = None
    number_50_coin = None
    number_100_coin = None

    def __init__(self, coins: list = None):
        if coins is None:
            coins = [0, 1, 2, 3]

        print("coins", coins)
        self.number_10_coin = coins[0]
        self.number_20_coin = coins[1]
        self.number_50_coin = coins[2]
        self.number_100_coin = coins[3]

    def get_total(self):
        total: int = 0
        total = total + self.number_10_coin
        total = total + self.number_20_coin
        total = total + self.number_50_coin
        total = total + self.number_100_coin

        return total