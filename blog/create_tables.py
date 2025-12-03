# test_sqlalchemy.py
from blog.database import SessionLocal
from blog.models.user import User
from blog.models.post import Post
from blog.models.comment import Comment

session = SessionLocal()

new_user = User(username="testuser", email="test@example.com", password_hash="12345")
session.add(new_user)
session.commit()

print("User inserted successfully!")
