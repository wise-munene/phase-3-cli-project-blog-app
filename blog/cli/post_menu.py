#blog/cli/post_menu.py
from blog.database import SessionLocal
from services.post_service import (
    create_post,
    get_post_by_id,
    get_all_posts,
    update_post,
    delete_post
)   

def post_menu(logged_in_user_id: int):
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
            db = SessionLocal()
            post = create_post(db, title, content, logged_in_user_id) #what this does is to create a post associated with the logged-in user
            db.close()
            print(f"Post created with ID: {post.id}")

        elif choice == '2':
            post_id = int(input("Enter post ID: ")) # Get post ID from user
            db = SessionLocal()
            post = get_post_by_id(db, post_id)  # Retrieve the post by ID
            db.close()
            if post:
                print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")
            else:
                print("Post not found.")

        elif choice == '3':
            db = SessionLocal()
            posts = get_all_posts(db)
            db.close()
            for post in posts:  # Iterate through all posts
                print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")   # Display each post

        elif choice == '4':
            post_id = int(input("Enter post ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            content = input("Enter new content (leave blank to keep current): ")
            db = SessionLocal()
            success, message = update_post(db, post_id, title or None, content or None)
            print(message)
            db.close()

        elif choice == '5':
            post_id = int(input("Enter post ID to delete: "))
            db = SessionLocal()
            success, message = delete_post(db, post_id)
            print(message)
            db.close()

        elif choice == '6':
            print("Exiting Post Menu...")
            break

        else:
            print("Invalid option. Please try again.")



