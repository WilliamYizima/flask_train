from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20))
    email = db.Column(db.String(20))
    idade = db.Column(db.Integer)

    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def serialize(self):
        return{
            'id': self._id,
            'name': self.nome,
            'email': self.email,
            'idade': self.idade
        }
