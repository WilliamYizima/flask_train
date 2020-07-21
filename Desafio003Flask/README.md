# Rede Social Fundo de Quintal
##Escopo
### 1. Funcionalidades

- [ ] Cadastro de usuários
- [ ] Login de usuários(A)
- [ ] Post de usuários(A)
- [ ] Comment de usuários(B)
- [ ] Feed (List dos posts de todos os usuários)
- [ ] Mostrar perfil do usuário 
- [ ] Mandar email de cadastro

### 2. Telas
- [ ] Login
- [ ] Cadastro
- [ ] Feed,comment
- [ ] Post
- [ ] Perfil

### 3. BD
- [ ] User
    - Nome
    - Sobrenome
    - email
    - senha
    - idade
    - Gostos
    - foto(???)
- [ ] Post
    - titulo
    - data
    - conteudo
    - foto (???)
    - **Usuário**
    - **Comentário**
    - n curtida
    - n descurtida
- [ ] Coment
    - **Usuário**
    - data
    - conteudo

### 4. Passos
- [ ] BD -> postgreSQL
- [ ] Back-end -> Flask 
- [ ] Front-end -> Flask
- [ ] Cloud - Heroku

---
# Passo-a-Passo

1. Criando o BD & 1 Deploy
- Necessário:
    - POSTGRESQL
    - Tudo entre 'bash', digite no terminal
    - GIT
    - Crie um ambiente virtual
    - Heroku instalado

- insira os requirements
```bash
    pip install -r requirements.txt
```

- criando a db
```bash
    sudo -u name_user createdb yorkut
```
- verificando se criou
```bash
    psql -U name_user -d yorkut
```
- para sair do terminal do psql
```bash
    \q
```
- Para utilizar a configuração de desenvolvimento conforme o arquivo config.py:
```bash
    export APP_SETTINGS="config.DevelopmentConfig"
```
- para expôr a variável DABA_BASE, digite:
```bash
    export DATABASE_URL="postgresql:///yorkut"
```
- para executar o FLASK:
```bash
    FLASK_APP=app.py flask run
```
- rode o manage.py para iniciar a migração(irá criar uma pasta migrations):
```bash
    python manage.py db init
```
- rode o manage.py novamente para migrate
```bash
    python manage.py db migrate
```
- Atualizando conforme seu models
```bash
    python manage.py db upgrade
```
- verifique o resultado
```bash
    psql -U name_user -d yorkut
    \dt
    \d tb_user
```
- crie um arquivo Proffile (sem extensão) para a comunicação com o heroku,com esse conteúdo:
'web: gunicorn app:app'

- crie um arquivo runtime.txt com esse conteúdo:
'python-3.6.5'

- crie uma aplicação no heroku:
```bash
    heroku create name_application
```
- coloque o repositório remoto do heroku(no caso dei o nome do meu repo de hiro):
```bash
    git remote add hiro https://git.heroku.com/yorkut.git
```

- faça a config no heroku:
```bash
    heroku config:set APP_SETTINGS=config.ProductionConfig --remote hiro
```

- Crie um DB Postgres no Heroku:
```bash
    heroku addons:create heroku-postgresql:hobby-dev --app yorkut
```