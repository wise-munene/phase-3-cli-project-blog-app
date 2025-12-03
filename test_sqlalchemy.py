# test_sqlalchemy.py
from blog.database import SessionLocal
from blog.models.user import User
from blog.models.post import Post
from blog.models.comment import Comment

# Create a session
session = SessionLocal()

# Now that all models are loaded, we can safely create a User
new_user = User(
    username="testuser",
    email="test@example.com",
    password_hash="12345"
)

session.add(new_user)
session.commit()

print("User inserted successfully!")
