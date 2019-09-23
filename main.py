from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Todo1', 'Todo2', 'Todo3', 'todo4', 'todo5']

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