from Helpers.MachineHelper import MachineHelper


class VendingMachine(MachineHelper):
    def display_items(self) -> None:
        """Display snacks items in the machine."""
        pass

    def select_item(self, item_no: int) -> bool:
        """Pick the item by proving it's id, return True if found."""
        pass

    def enter_coins(self, coins: list) -> None:
        """Enter the coins list"""
        pass
