from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

#config
app.config['MONGO_URI'] = 'mongodb://localhost:27017/teste01'

mongo = PyMongo(app)

@app.route('/')
def rota_teste():
    usuario = mongo.db.collection_teste.find()
    usuario_teste = mongo.db.collection_teste.find().limit(10)
    print(type(usuario_teste))
    resposta = dumps(usuario)

    return render_template('lista.html', lista=usuario_teste)

@app.route('/novo', methods=['GET','POST'])
def rota2():
    if request.method == 'GET':
        return render_template('formulario.html')
    else:
        nome = request.form['nome_usuario']
        senha = request.form['senha']
        email = request.form['email']

        mongo.db.collection_teste.insert({'nome': nome, 'senha': senha, 'email': email})
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)


