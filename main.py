from key_manager import KeyManager


def main():
    manager = KeyManager()

    while True:
        print("\nAPI Key Manager")
        print("1. Generate Key")
        print("2. List Active Keys")
        print("3. Revoke Key")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            key = manager.generate_key()
            print("Generated Key:", key)

        elif choice == "2":
            keys = manager.list_active_keys()
            for k in keys:
                print(k["key"])

        elif choice == "3":
            key_value = input("Enter key to revoke: ")
            manager.revoke_key(key_value)
            print("Key revoked.")

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()