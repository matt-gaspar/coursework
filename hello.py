from flask import Flask
from flask import request, g, session, render_template, redirect, url_for, flash
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'
bootstrap = Bootstrap(app)


class LoginForm(Form):
    username = StringField('User Name :', validators=[Required()])
    password = PasswordField('Password :', validators=[Required()])
    submit = SubmitField('Login')


@app.before_request
def loadUsers():
    userdict = {}
    with open("users.txt", 'rt') as f:
        line = f.readline()
        while line:
            [username, password] = line.rstrip().split(',')
            userdict[username] = password
            line = f.readline()
    g.userdict = userdict


@app.route('/routes')
def routes():
    out = []
    routes = app.url_map.iter_rules()
    for r in routes:
        out.append(str(r))
    return render_template('routes.html', routes=out)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/healthcheck')
def healthcheck():
    return "Status OK"


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = None
    password = None
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data
            ok = g.userdict.get(username) == password
            if ok:
                session[username] = username
                return render_template('login_result.html', name=username)
            else:
                flash('Login Incorrect')
                return render_template('login_form.html', form=form, username=username, password=password)
    return render_template('login_form.html', form=form, username=username, password=password)


@app.route('/listusers')
def listUsers():
    return render_template('userlist.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
