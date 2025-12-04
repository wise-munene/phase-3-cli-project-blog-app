from blog.database import SessionLocal
from blog.models.user import User

def get_user_by_id(db, user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

def get_user_by_username(db, username: str):
    session = SessionLocal()
    user = session.query(User).filter(User.username == username).first()
    session.close()
    return user

def list_all_users(db):
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def delete_user(db, user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        session.close()
        return False, "User not found."
    
    session.delete(user)
    session.commit()
    session.close()
    return True, "User deleted successfully."

def update_email(db, user_id: int, new_email: str):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        session.close()
        return False, "User not found."
    
    user.email = new_email
    session.commit()
    session.refresh(user)
    session.close()
    return True, "Email updated successfully."