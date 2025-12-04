from sqlalchemy.orm import Session
from blog.models.comment import Comment
from blog.models.post import Post

def add_comment(db: Session, post_id: int, user_id: int, content: str):
    post= db.query(Post).filter(Post.id == post_id).first()  # Check if the post exists
    if not post:
        return None, "Post not found."
    
    new_comment = Comment(post_id=post_id, user_id=user_id, content=content)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment, "Comment added successfully."

def get_comments_by_post_id(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()  # Retrieve comments for a specific post

def delete_comment(db: Session, comment_id: int, user_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.user_id == user_id).first()
    if not comment:
        return False, "Comment not found or you do not have permission to delete this comment."
    
    db.delete(comment)
    db.commit()
    return True, "Comment deleted successfully."