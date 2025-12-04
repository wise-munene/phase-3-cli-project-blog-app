from sqlalchemy.orm import Session
from blog.models import Post

def create_post(db: Session, title: str, content: str, user_id: int):
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()# Retrieve a post by its ID

def get_all_posts(db: Session):
    return db.query(Post).all()  # Retrieve all posts

def update_post(db: Session, post_id: int, title: str = None, content: str = None): 
    post = db.query(Post).filter(Post.id == post_id).first()
    if  not post:
        return False, "Post not found."
    if title is not None:
        post.title= title 
    if content is not None:
        post.content = content
    db.commit()
    db.refresh(post)
    return True, "Post updated successfully."


def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return False, "Post not found."
    db.delete(post)
    db.commit()
    return True, "Post deleted successfully."
        