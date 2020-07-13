from mongoengine import connect, Document, StringField, FloatField

connect('pokemon', host='mongodb://localhost:27017/desafio02')


class Pokemon(Document):
    name = StringField(required=True)
    price = FloatField(required=True)
    description = StringField(required=True)


