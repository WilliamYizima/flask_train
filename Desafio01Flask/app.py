from flask import Flask, render_template
from flask_bootstrap import Bootstrap


from data_person.dados import data_person

app = Flask(__name__)
Bootstrap(app)

my_data = data_person()

@app.route('/')
def index():
    list_person = data_person()
    return render_template('index.html',
                           list_person=list_person)


if __name__ == '__main__':
    app.run(debug=True)