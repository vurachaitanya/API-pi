# My first Rest API 
# Need python && pip install flask-restful


from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Chaitu",
        "age": 42,
        "occupation": "Software"
    },
    {
        "name": "Bindhu",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Anuradha",
        "age": 22,
        "occupation": "Housewife"
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)

