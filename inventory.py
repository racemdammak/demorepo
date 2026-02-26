from storage import load_inventory, save_inventory


class Inventory:
    def __init__(self):
        self.items = load_inventory()

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

        save_inventory(self.items)

    def reduce_stock(self, name, quantity):
        if name in self.items:
            # Hidden bug: can go negative
            self.items[name] -= quantity 
            save_inventory(self.items)

    def delete_item(self, name):
        # Hidden bug: KeyError if missing
        del self.items[name]
        save_inventory(self.items)