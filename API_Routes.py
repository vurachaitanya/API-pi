## Usage :  python API_Routes.py & ; curl http://127.0.0.1:5000/ ; curl http://127.0.0.1:5000/login

import flask

app = flask.Flask(__name__)
#app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Welcome to API World"

@app.route('/login', methods=['GET'])
def login():
    return "Welcome to API login"

@app.route('/api/v1/users/', methods=['GET', 'POST'])
def user():
    return "Welcome to API users-versions"

app.run(debug=True)
## Source : https://hackersandslackers.com/flask-routes/
