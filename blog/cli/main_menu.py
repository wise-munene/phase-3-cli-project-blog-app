from blog.cli.post_menu import post_menu
from blog.cli.auth_menu import auth_menu
from blog.cli.comment_menu import comment_menu
from blog.cli.user_menu import user_menu



def main_menu():
    logged_in_user = auth_menu()  # Initial authentication

    while True:
        print("\n=== Main Menu ===")
        print("1. Authentication Menu")
        print("2. Post Menu")
        print("3. Comment Menu")
        print("4. User Menu")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            logged_in_user= auth_menu()
            if logged_in_user:
                logged_in_user = logged_in_user  # Update logged-in user if authentication is successful

        elif choice == '2' :
            if logged_in_user:
                post_menu(logged_in_user.id)  # Pass the logged-in user to the post menu
            else:
                print("You must be logged in to access the Post Menu.")
                continue
        elif choice == '3' :
            if logged_in_user:
                comment_menu(logged_in_user.id)  # Pass the logged-in user to the comment menu
            else:
                print("You must be logged in to access the Comment Menu.")
                continue

        elif choice == '4' :
            if logged_in_user:
                logged_in_user = user_menu(logged_in_user)  # Pass the logged-in user to the user menu and update if changed
            else:
                print("You must be logged in to access the User Menu.")
                continue

        elif choice == '5':
            print("Exiting the application...")
            break

        else:
            print("Invalid option. Please try again.")