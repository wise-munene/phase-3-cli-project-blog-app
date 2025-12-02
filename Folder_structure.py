import os

# List of folders to create
folders = [
    "blog",
    "blog/models",
    "blog/cli",
    "blog/toolbox"
]

# List of files to create
files = [
    "app.py",
    "README.md",
    "blog/__init__.py",
    "blog/database.py",
    "blog/seed.py",
    "blog/models/__init__.py",
    "blog/models/user.py",
    "blog/models/post.py",
    "blog/models/comment.py",
    "blog/cli/__init__.py",
    "blog/cli/main_menu.py",
    "blog/cli/auth_menu.py",
    "blog/cli/user_menu.py",
    "blog/cli/post_menu.py",
    "blog/cli/comment_menu.py",
    "blog/toolbox/__init__.py",
    "blog/toolbox/hashing.py",
    "blog/toolbox/validations.py",
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Folder created: {folder}")

# Create files
for file in files:
    with open(file, "w") as f:
        f.write("")  # Create empty file
    print(f"File created: {file}")

print("\nFolder structure generated successfully!")
