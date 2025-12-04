from blog.database import SessionLocal
from blog.models.user import User

def get_user_by_id(db, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return user

def get_user_by_username(db, username: str):
    user = db.query(User).filter(User.username == username).first()
    return user

def list_all_users(db):
    users = db.query(User).all()
    return users

def delete_user(db, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return False, "User not found."
    
    db.delete(user)
    db.commit()
    return True, "User deleted successfully."

def update_user_email(db, user_id: int, new_email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return False, "User not found."
    
    user.email = new_email
    db.commit()
    db.refresh(user)
    return True, "Email updated successfully."