#blog/services/auth_service.py

from blog.models.user import User
from blog.toolbox.hashing import hash_password, verify_password
from blog.database import SessionLocal

def create_user(username: str, email: str, plain_password: str) -> User:  #user means it returns a user object

    session=SessionLocal()

    if session.query(User).filter((User.username == username) | (User.email == email)).first():
        session.close()
        return False, "Username or email exists"
    
    password_hash = hash_password(plain_password)
    new_user = User(username=username, email=email, password_hash=password_hash)
    session.add(new_user)
    session.commit()   #commit the transaction to the database
    session.refresh(new_user) #refresh the instance with the latest data from the database
    session.close()
    return True, "User created successfully"


def authenticate_user(username: str, plain_password: str) -> bool:  #checks if the username and password are correct

    session=SessionLocal()
    user= session.query(User).filter(User.username == username).first()   #get the user from the database

    if not user:
        session.close()
        return False, "User not found"
    
    if verify_password(plain_password, user.password_hash):
        session.close()
        return True, "Authentication successful"
    else:
        session.close()
        return False, "Incorrect password"