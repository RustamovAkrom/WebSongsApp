from app import db
from flask import url_for
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
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    avatar = db.Column(db.String(255), default="avatars/default/default.jpg")

    def image_url(self):
        if self.avatar:
            return url_for('static', filename='avatars/' + self.avatar)
        else:
            return url_for('static', filename='avatars/default/default.jpg')
        
    def __repr__(self) -> str:
        return f"User('{self.username}' '{self.email}')"
    

class Song(AbstractBaseModel):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    image = db.Column(db.String(255), nullable=True, default = 'songs/default/default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", backref = db.backref("users", uselist=False))

    def __repr__(self) -> str:
        return f"Song('{self.title}')"
    