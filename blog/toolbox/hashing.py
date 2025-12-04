#toolbox/hashing.py
import bcrypt


def hash_password(password: str) -> str: #checks for password type str and returns str

    """Hash a password for storing."""
    password_bytes = password.encode('utf-8')  #convert to bytes becaise bycrypt works with bytes
    salt = bcrypt.gensalt()   #generate a salt, a salt is random data that is used as an additional input to a one-way function that "hashes" a password or passphrase
    hashed = bcrypt.hashpw(password_bytes, salt)   #hash the password with the salt, hash means to convert the password into a fixed-size string of characters, which is typically a sequence of numbers and letters
    return hashed.decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:  #bool means it returns true or false wherether the password matches the hash

    """Verify a stored password against one provided by user."""
    password_bytes = password.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

