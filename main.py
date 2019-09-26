from flask import Flask, request, make_response, redirect, render_template

todos = ['Compra', 'Ejercicio', 'trabajar', 'Dormir', 'Repetir']

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

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