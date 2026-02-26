from inventory import Inventory


def main():
    inv = Inventory()

    while True:
        print("\nMini Inventory Tracker")
        print("1. Add Item")
        print("2. Reduce Stock")
        print("3. Delete Item")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Item name: ")
            qty = int(input("Quantity: "))
            inv.add_item(name, qty)
            print("Item added.")

        elif choice == "2":
            name = input("Item name: ")
            qty = int(input("Quantity to reduce: "))
            inv.reduce_stock(name, qty)
            print("Stock reduced.")

        elif choice == "3":
            name = input("Item name: ")
            inv.delete_item(name)
            print("Item deleted.")

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()