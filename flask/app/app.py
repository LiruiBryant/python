from flask import Flask
from flask import request
from flask import current_app
from flask import app
from flask import make_response
from flask import *

app = Flask(__name__)


# @app.route('/')
# @app.route('/index')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' % user_agent

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name


@app.route('/bad')
def bad():
    return '<h1>Bad Request</h1>', 400


@app.route('/bad_request')
def bad_request():
    response = make_response('<h1>Bad Request</h1>')
    response.set_cookie('answer', 42)
    return response


@app.route('/redirect')
def redirect():
    return redirect('http://earyant.github.io')


@app.route('/user/<id>')
def get_user(id):
    if id == 1:
        abort(404)
    return '<h1>hello</h1>'


if __name__ == '__main__':
    app.run(debug=True)
