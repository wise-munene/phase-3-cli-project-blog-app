#blog/cli/comment_menu.py
from blog.database import SessionLocal
from services.comment_service import (
    add_comment,
    get_comments_by_post_id,
    delete_comment
)

def comment_menu(logged_in_user_id):
    db = SessionLocal()    # Create a new database session
    while True:
        print("\n=== Comment Menu ===")
        print("1. Add Comment")
        print("2. View Comments by Post ID")
        print("3. Delete Comment")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            post_id = int(input("Enter post ID to comment on: "))
            content = input("Enter your comment: ")
            comment, message = add_comment(db, post_id, logged_in_user_id, content)
            print(message)

        elif choice == '2':
            post_id = int(input("Enter post ID to view comments: "))
            comments = get_comments_by_post_id(db, post_id)
            for comment in comments:
                print(f"Comment ID: {comment.id}, User ID: {comment.user_id}, Content: {comment.content}")

        elif choice == '3':
            comment_id = int(input("Enter comment ID to delete: "))
            success, message = delete_comment(db, comment_id, logged_in_user_id)
            print(message)

        elif choice == '4':
            print("Exiting Comment Menu...")
            break

        else:
            print("Invalid option. Please try again.")

