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
        if name not in self.items:
            print("Error: Item does not exist.")
            return False

        if quantity < 0:
            print("Error: Quantity must be positive.")
            return False

        if self.items[name] - quantity < 0:
            print("Error: Cannot reduce stock below zero.")
            return False

        self.items[name] -= quantity
        save_inventory(self.items)
        return True

    def get_item(self, name):
        # BUG (TST-102): Raises KeyError if item doesn't exist
        return self.items[name]