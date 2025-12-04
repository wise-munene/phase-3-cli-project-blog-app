from services.auth_service import create_user, authenticate_user


def create_account():
    print("=== Create Account ===")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    success, message = create_user(username, email, password)
    print(message)

def login():
    print("=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    success, message = authenticate_user(username, password)
    print(message)

    if success:
        return username  # Return the logged-in username
    return None

def auth_menu():
    logged_in_user = None # Variable to track logged-in user so we can use it later

    while True:
        print("\n=== Authentication Menu ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            logged_in_user = login()
            if logged_in_user:
                break  # Exit the loop if login is successful
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")