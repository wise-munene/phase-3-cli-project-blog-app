from blog.cli.post_menu import post_menu
from blog.cli.auth_menu import auth_menu



def main_menu():
    logged_in_user = None

    while True:
        print("\n=== Main Menu ===")
        print("1. Authentication Menu")
        print("2. Post Menu")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            logged_in_user= auth_menu()
            if logged_in_user:
                logged_in_user = logged_in_user  # Update logged-in user if authentication is successful

        elif choice == '2' and logged_in_user:
            post_menu(logged_in_user)  # Pass the logged-in user to the post menu

        elif choice == '3' and logged_in_user:
            logged_in_user = None
            print("Logged out successfully.")
            break

