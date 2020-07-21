from flask import render_template, request, jsonify, redirect, url_for
from . import main
from db.models import User, db
from db.models import Post, db
from flask_login import login_required, current_user

@main.route('/')
def index():

    if current_user.is_anonymous == True:
        return render_template('inicial.html')
    else:
        return redirect(url_for('main.login_index'))



@main.route('/secret')
@login_required
def secret():
    return 'rolou'


@main.route('/add')
def add_user():
    name = request.args.get('name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    senha = request.args.get('senha')
    age = request.args.get('age')
    hobby = request.args.get('hobby')

    try:
        user = User(
            name=name,
            last_name=last_name,
            email=email,
            password_hash=senha,
            age=age,
            hobby=hobby
        )
        user.password = senha
        db.session.add(user)
        db.session.commit()
        return "user added, user id={}".format(user.id)
    except Exception as e:
        return (str(e))


@main.route('/getall')
def get_all():
    try:
        users = User.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return (str(e))

@main.route('/home')
@login_required
def login_index():
    try:
        posts = Post.query.all()
        print(posts)
        post_serialize = [e.serialize() for e in posts]
        print(post_serialize)
        return render_template('auth/index.html', data_post=post_serialize)
    except Exception as e:
        return (str(e))
    return render_template('auth/index.html')



@main.route('/cadastro', methods=['GET', 'POST'])
def add_user_form():
    if request.method == 'POST':
        name = request.form.get('name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        senha = request.form.get('senha')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        try:
            user = User(
                name=name,
                last_name=last_name,
                email=email,
                password_hash=senha,
                age=age,
                hobby=hobby
            )
            user.password = senha
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception as e:
            return (str(e))

    return render_template('cadastro.html')

@main.route('/perfil')
@login_required
def profile():
    user = User.query.filter_by(id=current_user.get_id()).first()

    return render_template('auth/perfil.html',data_user=user)

@main.route('/modificar', methods=['POST'])
def edit_user():
    if request.method == 'POST':
        name = request.form.get('name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        senha = request.form.get('senha')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        try:
            user = User.query.filter_by(id=str(current_user)).first()
            user.name = name
            user.last_name = last_name
            user.email = email
            user.password_hash = senha
            user.age = age
            user.hobby = hobby

            user.password = senha

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.profile'))
        except Exception as e:
            return (str(e))
