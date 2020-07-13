from flask import Flask, render_template

app = Flask(__name__)
PORT = 5000


listaDeFilmes = ['Tropa de elite', 'A rede social', 'Fome de poder','item 04','item 05','item 08',' ESSE É O ÚLTIMO FILME']
@app.route('/')
def rota1():
    return render_template('index.html', lista=listaDeFilmes)


@app.route('/login')
def rota2():
    return render_template('login.html')


@app.route('/<int:id>')
def rota3(id):
    return render_template('testao.html', id=id)


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
