from app import db
from app import login_manager

from datetime import datetime


class AbstractBaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(AbstractBaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    login = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=True)
    avatar = db.Column(db.String(255), default="avatars/default/default.jpg", nullable=True)

    def __repr__(self) -> str:
        return f"User('{self.username}' '{self.email}')"
    

class Song(AbstractBaseModel):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    image = db.Column(db.String(255), nullable=True, default = 'songs/default/default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True, nullable=True)

    def __repr__(self) -> str:
        return f"Song('{self.title}')"
    