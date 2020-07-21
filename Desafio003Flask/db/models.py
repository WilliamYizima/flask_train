from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class User(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    hobby = db.Column(db.String(), nullable=False)
    pk_post = db.relationship('Post', uselist=False, backref='tb_user', lazy=True)
    pk_comment = db.relationship('Comment', uselist=False, backref='tb_user', lazy=True)

    def __init__(self, name, last_name, email, password_hash, age, hobby):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password_hash = password_hash
        self.age = age
        self.hobby = hobby

    def __repr__(self):
        return '{}'.format(self.id)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password_hash,
            'age': self.age,
            'hobby': self.hobby
        }

    def is_authenticated(self):
        return True

    def is_active(self):  # line 37
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Post(db.Model):
    __tablename__ = 'tb_post'

    id_post = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(), nullable=False)
    updated_at = db.Column(db.Date(), onupdate=datetime.datetime.now(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    count_like = db.Column(db.String(128), nullable=False)
    count_dislike = db.Column(db.Integer(), nullable=False)
    fg_user = db.Column(db.Integer, db.ForeignKey('tb_user.id'), nullable=False)
    pk_comment = db.relationship('Comment', uselist=False, backref='tb_post',lazy=True)

    def serialize(self):
        return {
            'id_post': self.id_post,
            'titulo': self.titulo,
            'updated_at': self.updated_at,
            'content': self.content,
            'count_like': self.count_like,
            'count_dislike': self.count_dislike,
            'fg_user': self.fg_user,
            'pk_comment':self.pk_comment
        }

class Comment(db.Model):
    __tablename__ = 'tb_comment'

    id_comment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    updated_at = db.Column(db.Date(), onupdate=datetime.datetime.now(), nullable=False)
    fg_user = db.Column(db.Integer, db.ForeignKey('tb_user.id'), nullable=False)
    fg_post = db.Column(db.Integer, db.ForeignKey('tb_post.id_post'), nullable=False)
