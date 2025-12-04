from blog.database import SessionLocal
from services.user_service import (
    get_user_by_username,
    get_user_by_id,
    list_all_users,
    delete_user,
    update_user_email,
)

def user_menu(logged_in_user):
    db = SessionLocal()
    try:
       print(f"logged in as:{logged_in_user.username}{logged_in_user.email}\n")
        
       while True:
         print("\n=== User Menu ===")
         print(f"logged in as: {logged_in_user.username}{logged_in_user.email}\n")
         print("1. View User by ID")
         print("2. View User by Username")
         print("3. List All Users")
         print("4. Delete User")
         print("5. Update User Email")
         print("6. Exit")
         choice = input("Select an option: ")
         if choice == '1':
            user=get_user_by_id(db,logged_in_user.id) # Retrieve user by ID
            print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")

         elif choice == '2':
            username = input("Enter username: ")
            user = get_user_by_username(db,username) # Retrieve user by username
            if user:  # Check if user exists
                print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")
            else:
                print("User not found.")

         elif choice == '3':
            users = list_all_users(db)  # Retrieve all users
            for user in users:
                print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")
              # Update the email in the logged-in user object

         elif choice == '4':
            confirm = input("Are you sure you want to delete your account? (yes/no): ")
            if confirm.lower() == 'yes':
                success, message = delete_user(db, logged_in_user.id)
                print(message)
                if success:
                    print("logging out...")
 
         elif choice == '5':
            new_email = input("Enter new email: ")
            success, message = update_user_email(db, logged_in_user.id, new_email)
            print(message)
            if success:
                logged_in_user.email = new_email  # Update the email in the logged-in user object
                     
        
         elif choice == '6':
            return logged_in_user # Exit the user menu and return to main menu
         else:
            print("Invalid option. Please try again.")

    finally:
        db.close()