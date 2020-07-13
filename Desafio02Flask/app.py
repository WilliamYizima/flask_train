import re
import os

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from mongoengine import connect, Document, StringField, FloatField, FileField

app = Flask(__name__)

Bootstrap(app)

connect('pokemon', host='mongodb://localhost:27017/desafio02')
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/static/img'


class Pokemon(Document):
    name = StringField(required=True)
    price = FloatField(required=True)
    description = StringField(required=True)
    imagem = FileField()
#TODO imagem é opcional

@app.route('/')
def index():
    pokemon_list = Pokemon.objects

    return render_template('index.html', lista_pokemon=pokemon_list)


@app.route('/find', methods=["POST"])
def find():
    _name = request.form['name']
    regex = re.compile(f'.*{_name}.*')
    pokemon_name = Pokemon.objects(name=regex)
    print(pokemon_name)
    return render_template('index.html', lista_pokemon=pokemon_name)


@app.route('/detail/<string:_id>')
def detail(_id):
    pokemon_id = Pokemon.objects(id=_id)
    return render_template('detail.html', variavel=pokemon_id[0])


# TODO inserir imagem
# TODO transformar em base64 e escrever no banco
@app.route('/create', methods=['POST'])
def create():
    name = request.form['nome']
    price = request.form['preco']
    descrip = request.form['descricao']
    arquivo_recebido = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo_recebido.save(f'{upload_path}/{arquivo_recebido.filename}')
    pokemon_create = Pokemon(name=name,
                             price=price,
                             description=descrip)
    pokemon_create.save()
    return redirect(url_for('index'))


@app.route('/modify', methods=['PUT', 'POST'])
def modify():
    if (request.method == "PUT") or (request.method == "POST"):
        name = request.form['nome']
        price = request.form['preco']
        descrip = request.form['descricao']
        _id = request.form['id']
        print('passei aqui')

        pokemon_update = Pokemon.objects(id=_id)
        pokemon_update.update(
            name=name,
            price=price,
            description=descrip
        )
        return redirect(url_for('detail', _id=_id))


# TODO colocar post
@app.route('/delete/<string:_id>', methods=['DELETE', 'POST'])
def delete(_id):
    if (request.method == "DELETE") or (request.method == "POST"):
        pokemon_update = Pokemon.objects(id=_id)
        pokemon_update.delete()
        return jsonify({"message": "ok"})


if __name__ == '__main__':
    app.run(debug=True)
