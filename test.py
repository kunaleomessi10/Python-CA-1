
from test import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class helloworld(Resource):
    def get(self):
        return {"data" : "Helloworld"}

api.add_resource(helloworld,"/helloworld")

if __name__ == "__main__":
    app.run(debug=True)