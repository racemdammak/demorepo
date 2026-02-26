from storage import load_inventory, save_inventory, generate_inventory_checksum


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
    
    # in this function we will be calling our legacy code unit: so it can be detected as a conflict.
    def verify_integrity(self):
        """
        Verifies current inventory integrity using legacy checksum function.
        """
        current_checksum = generate_inventory_checksum(self.items)
        print(f"Current Inventory Checksum: {current_checksum}")
        return current_checksum