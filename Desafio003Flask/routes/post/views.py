from flask import render_template, request, jsonify, redirect, url_for
from . import post
from db.models import Post, db
from flask_login import login_required, current_user
import datetime

@post.route('/getall')
@login_required
def get_all_post():
    try:
        users = Post.query.all().order_by(desc(Post.updated_at))
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return (str(e))



@post.route('/cadastro', methods=['POST'])
@login_required
def add_post_form():
    print(current_user.get_id())
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        postagem = request.form.get('postagem')
        email = request.form.get('email')
        senha = request.form.get('senha')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        try:
            post = Post(
                titulo=titulo,
                content=postagem,
                count_like=0,
                count_dislike=0,
                updated_at=datetime.datetime.now(),
                fg_user=int(current_user.get_id())
            )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('main.login_index'))
        except Exception as e:
            return (str(e))
    return 'deu erro'

@post.route('/like/<int:id>')
@login_required
def like_post(id):
    try:
        post = Post.query.filter_by(id_post=str(id)).first()
        print(type(post.count_like))
        like = int(post.count_like) + 1
        post.count_like = like
        db.session.commit()
        return redirect(url_for('main.login_index'))
    except Exception as e:
        return (str(e))

@post.route('/dislike/<int:id>')
@login_required
def dislike_post(id):
    try:
        post = Post.query.filter_by(id_post=str(id)).first()
        dislike = int(post.count_dislike) + 1
        post.count_dislike = dislike
        db.session.commit()
        return redirect(url_for('main.login_index'))
    except Exception as e:
        return (str(e))

# @main.route('/home')
# @login_required
# def login_index():
#     return render_template('auth/index.html')
#


#
# @main.route('/')
# def index():
#     if current_user.is_anonymous == True:
#         return render_template('inicial.html')
#     else:
#         return redirect(url_for('main.login_index'))
#
#
#
# @main.route('/secret')
# @login_required
# def secret():
#     return 'rolou'
#
#
# @main.route('/add')
# def add_user():
#     name = request.args.get('name')
#     last_name = request.args.get('last_name')
#     email = request.args.get('email')
#     senha = request.args.get('senha')
#     age = request.args.get('age')
#     hobby = request.args.get('hobby')
#
#     try:
#         user = User(
#             name=name,
#             last_name=last_name,
#             email=email,
#             password_hash=senha,
#             age=age,
#             hobby=hobby
#         )
#         user.password = senha
#         db.session.add(user)
#         db.session.commit()
#         return "user added, user id={}".format(user.id)
#     except Exception as e:
#         return (str(e))
#
#
#


# @main.route('/perfil')
# @login_required
# def profile():
#     user = User.query.filter_by(id=current_user.get_id()).first()
#
#     return render_template('auth/perfil.html',data_user=user)
#
# @main.route('/modificar', methods=['POST'])
# def edit_user():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         last_name = request.form.get('last_name')
#         email = request.form.get('email')
#         senha = request.form.get('senha')
#         age = request.form.get('age')
#         hobby = request.form.get('hobby')
#         try:
#             user = User.query.filter_by(id=str(current_user)).first()
#             user.name = name
#             user.last_name = last_name
#             user.email = email
#             user.password_hash = senha
#             user.age = age
#             user.hobby = hobby
#
#             user.password = senha
#
#             db.session.add(user)
#             db.session.commit()
#             return redirect(url_for('main.profile'))
#         except Exception as e:
#             return (str(e))
