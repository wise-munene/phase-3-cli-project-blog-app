#blog/cli/post_menu.py
from blog.database import SessionLocal
from services.post_service import (
    create_post,
    get_post_by_id,
    get_all_posts,
    update_post,
    delete_post
)   

def post_menu(logged_in_user_id):
    db = SessionLocal()    # Create a new database session, sesssion is a 
    while True:
        print("\n=== Post Menu ===")
        print("1. Create Post")
        print("2. View Post by ID")
        print("3. View All Posts")
        print("4. Update Post")
        print("5. Delete Post")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            post = create_post(db, title, content, logged_in_user_id) #what this does is to create a post associated with the logged-in user
            print(f"Post created with ID: {post.id}")

        elif choice == '2':
            post_id = int(input("Enter post ID: ")) # Get post ID from user
            post = get_post_by_id(db, post_id)  # Retrieve the post by ID
            if post:
                print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")
            else:
                print("Post not found.")

        elif choice == '3':
            posts = get_all_posts(db)
            for post in posts:  # Iterate through all posts
                print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")   # Display each post

        elif choice == '4':
            post_id = int(input("Enter post ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            content = input("Enter new content (leave blank to keep current): ")
            success, message = update_post(db, post_id, title or None, content or None)
            print(message)

        elif choice == '5':
            post_id = int(input("Enter post ID to delete: "))
            success, message = delete_post(db, post_id)
            print(message)

        elif choice == '6':
            print("Exiting Post Menu...")
            break

        else:
            print("Invalid option. Please try again.")

    db.close()

