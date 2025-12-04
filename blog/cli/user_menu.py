from services.user_service import (
    get_user_by_username,
    get_user_by_id,
    list_all_users,
    delete_user,
    update_email,
)

def user_menu(logged_in_user_id):
    while True:
        print("\n=== User Menu ===")
        print(f"logged in as: {logged_in_user_id.username}{logged_in_user_id.email}\n")
        print("1. View User by Username")
        print("2. View User by ID")
        print("3. List All Users")
        print("4. Delete User")
        print("5. Update User Email")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            user=get_user_by_id(logged_in_user_id)
            print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")

        elif choice == '2':
            username = input("Enter username: ")
            user = get_user_by_username(username) # Retrieve user by username
            if user:  # Check if user exists
                print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")
            else:
                print("User not found.")

        elif choice == '3':
            new_email = input("Enter new email: ")
            success, message = update_email(logged_in_user_id, new_email) # Update email for logged-in user, success means if the update was successful 
            print(message)
            if success:
                logged_in_user_id.email = new_email  # Update the email in the logged-in user object

        elif choice == '4':
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == 'yes':
                success, message = delete_user(logged_in_user_id)
                print(message)
                if success:
                    print("logging out...")
                    break  # Exit the user menu after deletion
        
        elif choice == '5':
            return logged_in_user_id  # Exit the user menu and return to main menu
        else:
            print("Invalid option. Please try again.")