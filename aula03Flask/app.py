from flask import Flask, render_template, request

app = Flask(__name__)

class Usuario:
    def __init__(self, nome, email, senha ):
        self.nome = nome
        self.email = email
        self.senha = senha

teste_01 = Usuario(nome='ahiufahsafhai', email='meuemail@hotmail.com', senha='katana')
teste_02 = Usuario(nome='Eita', email='aisfuhauf@hotmail.com', senha='afasfasf')

listinha = [teste_01, teste_02]

@app.route('/')
def rotaHome():
    return render_template('lista.html', lista=listinha)

@app.route('/newuser',methods=['POST'])
def novoUsuario():
    if request.method == 'POST':
        nome_input = request.form["nome_usuario"]
        senha_input = request.form["senha"]
        email_input = request.form["email"]

        usuario01 = Usuario(nome=nome_input,
                            email=email_input,
                            senha=senha_input)
        listinha.append(usuario01)
        return render_template('novouser.html', user=listinha)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

app.run(debug=True)