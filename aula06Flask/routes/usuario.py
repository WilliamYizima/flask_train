from flask import Blueprint, request, jsonify, current_app, render_template, redirect, url_for, current_app
from db.models import Usuarios

import re
import json

user = Blueprint('usuarios', __name__)


@user.route('/')
def index():
    try:
        usuario = Usuarios.query.all()
        all_user = [e.serialize() for e in usuario]
        print(all_user)
        return render_template('index.html',
                               obj=all_user)
    except Exception as e:
        return (str(e))


#TODO implantar o like
@user.route('/find', methods=["POST"])
def find():
    try:
        _name = request.form['name']
        usuario = Usuarios.query.filter_by(nome=_name).all()
        # obj = usuario.serialize()
        print(usuario)
        return render_template('index.html',
                           obj=usuario)
    except Exception as e:
        return (str(e))



@user.route('/detail/<string:_id>')
def detail(_id):

    usuario = Usuarios.query.filter_by(_id=_id).first()
    usuario = usuario.serialize()

    return render_template('detail.html', variavel=usuario)


# TODO inserir imagem
# TODO transformar em base64 e escrever no banco
@user.route('/create', methods=['POST'])
def create():

    name=request.form.get('nome')
    email=request.form.get('email')
    idade=request.form.get('idade')
    print(idade)
    try:
        usuario=Usuarios(
                nome=name,
                email=email,
                idade=int(idade)
        )
        current_app.db.session.add(usuario)
        current_app.db.session.commit()
        return redirect(url_for('usuarios.index'))

    except Exception as e:
        return(str(e))


@user.route('/modify', methods=['PUT', 'POST'])
def modify():
    if (request.method == "PUT") or (request.method == "POST"):
        _id = request.form['id']
        modify = Usuarios.query.filter(Usuarios._id == _id).first()

        name = request.form['nome']
        email = request.form['email']
        idade = request.form['idade']

        print(modify)
        modify_data = modify.nome(name)
        modify_data = modify.email(email)
        modify_data = modify.idade(idade)
        current_app.db.session.add(modify_data)
        current_app.db.session.commit()
        return redirect(url_for('detail', _id=_id))


# TODO colocar post
@user.route('/delete/<string:_id>', methods=['DELETE', 'POST'])
def delete(_id):
    if (request.method == "DELETE") or (request.method == "POST"):
        pokemon_update = Pokemon.objects(id=_id)
        pokemon_update.delete()
        return jsonify({"message": "ok"})

#
# @user.route('/detail/<string:_id>')
# def detail(_id):
#     pokemon_id = Pokemon.objects(id=_id)
#     return render_template('detail.html', variavel=pokemon_id[0])
