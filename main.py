from auth import AuthService


def main():
    auth = AuthService()

    while True:
        print("\nUser Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            auth.register(username, password)
            print("User registered.")

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            if auth.login(username, password):
                print("Login successful.")
            else:
                print("Invalid credentials.")

        elif choice == "3":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

    #test01