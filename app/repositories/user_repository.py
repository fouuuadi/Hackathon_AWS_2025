from app.models.user import User
from app.extensions import db

def get_by_username(username):
    return User.query.filter_by(username=username).first()

def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user