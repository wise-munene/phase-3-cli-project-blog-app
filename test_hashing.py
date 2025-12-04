from blog.toolbox.hashing import hash_password, verify_password

# Hash a password
plain_password = "mysecretpassword"
hashed_pw = hash_password(plain_password)
print("Hashed password:", hashed_pw)

# Verify correct password
if verify_password("mysecretpassword", hashed_pw):
    print("Password is correct!")
else:
    print("Password is wrong!")

# Verify incorrect password
if verify_password("wrongpassword", hashed_pw):
    print("Password is correct!")
else:
    print("Password is wrong!")
