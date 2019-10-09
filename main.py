from flask import Flask, request, make_response, redirect, render_template

todos = ['Compra', 'Ejercicio', 'trabajar', 'Dormir', 'Repetir']

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    return 'hello from here :)ss'

@app.route('/hello')
def hello():
    user_ip = request.remote_addr

    context = {
        'todo_list': todos,
        'user_ip': user_ip,
    }

    return render_template('hello.html', **context)

#emule error 500.
@app.route('/error')
def error():
    return 1 / 0
