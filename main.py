from inventory import Inventory


def main():
    inv = Inventory()

    while True:
        print("\nMini Inventory Tracker")
        print("1. Add Item")
        print("2. Reduce Stock")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Verify Inventory Integrity")
        print("6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Item name: ").strip()
            qty = int(input("Quantity: "))
            if inv.add_item(name, qty):
                print("Item added successfully.")

        elif choice == "2":
            name = input("Item name: ").strip()
            qty = int(input("Quantity to reduce: "))
            if inv.reduce_stock(name, qty):
                print("Stock reduced successfully.")

        elif choice == "3":
            name = input("Item name: ").strip()
            if inv.delete_item(name):
                print("Item deleted successfully.")

        elif choice == "4":
            items = inv.get_all_items()
            if not items:
                print("Inventory is empty.")
            else:
                print("\nCurrent Inventory:")
                for name, qty in items.items():
                    print(f"- {name}: {qty}")
                    
        elif choice == "5":
            inv.verify_integrity()

        elif choice == "6":
            break


if __name__ == "__main__":
    main()