from storage import load_inventory, save_inventory


class Inventory:
    def __init__(self):
        # Full persistence integration: load at startup
        self.items = load_inventory()

    def add_item(self, name, quantity):
        if quantity <= 0:
            print("Error: Quantity must be positive.")
            return False

        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

        save_inventory(self.items)
        return True

    def reduce_stock(self, name, quantity):
        """
        Reduces stock safely.
        Prevents:
        - Negative quantities
        - Negative inventory state
        - Operations on non-existing items
        """
        if name not in self.items:
            print("Error: Item does not exist.")
            return False

        if quantity <= 0:
            print("Error: Quantity must be positive.")
            return False

        if quantity > self.items[name]:
            print("Error: Cannot reduce stock below zero.")
            return False

        self.items[name] -= quantity
        save_inventory(self.items)
        return True

    def delete_item(self, name):
        """
        Deletes item safely.
        Prevents KeyError if item does not exist.
        """
        if name not in self.items:
            print("Error: Item does not exist.")
            return False

        del self.items[name]
        save_inventory(self.items)
        return True

    def get_all_items(self):
        return self.items.copy()