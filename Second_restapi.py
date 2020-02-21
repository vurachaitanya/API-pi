## Second RestAPI 
## Usage:  python Second_restapi.py & curl http://127.0.0.1:5000/occ/Software

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

occs = [
    {
        "name": "Chaitu",
        "age": 42,
        "occupation": "Software"
    },
    {
        "name": "Bindhu",
        "age": 32,
        "occupation": "housewife"
    },
    {
        "name": "Anuradha",
        "age": 22,
        "occupation": "Housewife"
    }
]

class Occ(Resource):
    def get(self, occupation):
        for occ in occs:
            if(occupation == occ["occupation"]):
                return occ, 200
        return "Occ not found", 404
api.add_resource(Occ, "/occ/<string:occupation>")

app.run(debug=True)
