from flask import Flask, render_template

app = Flask(__name__)

class Usuario:
    def __init__(self, nome, email, senha ):
        self.nome = nome
        self.email = email
        self.senha = senha

teste_01 = Usuario(nome='ahiufahsafhai', email='meuemail@hotmail.com', senha='katana')
teste_02 = Usuario(nome='Eita', email='aisfuhauf@hotmail.com', senha='afasfasf')

listinha = (teste_01,teste_02)

@app.route('/')
def rotaHome():
    return render_template('lista.html', lista=listinha)


app.run(debug=True)