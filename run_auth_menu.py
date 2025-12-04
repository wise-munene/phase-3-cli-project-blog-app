from blog.cli.auth_menu import auth_menu

def main():
    user = auth_menu()
    if user:
        print(f"User logged in: {user}")
    else:
        print("No user logged in.")

if __name__ == "__main__":
    main()
