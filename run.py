from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/home')
def home():
    return 'Welcome to HomePage!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Do Login'
    else:
        return 'LoginPage!'


if __name__ == '__main__':
    # app(host,port,debug)
    app.run(host='0.0.0.0', port='8888', debug=True)
