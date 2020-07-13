from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def rota1():
    return render_template('index.html')


@app.route('/login')
def rota2():
    return render_template('login.html')


@app.route('/<int:id>')
def rota3(id):
    return render_template('testao.html', id=id)

app.run(debug=True)
