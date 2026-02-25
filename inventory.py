from storage import load_inventory, save_inventory


class Inventory:
    def __init__(self):
        self.items = load_inventory()

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

        # BUG (TST-103): Missing save_inventory(self.items)

    def reduce_stock(self, name, quantity):
        if name in self.items:
            # BUG (TST-101): No validation for negative stock
            self.items[name] -= quantity
            save_inventory(self.items)

    def get_item(self, name):
        # BUG (TST-102): Raises KeyError if item doesn't exist
        return self.items[name]