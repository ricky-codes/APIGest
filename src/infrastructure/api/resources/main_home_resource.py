from flask_restful import Resource

class Main_Home(Resource):
    def get(self):
        return {"message": "Welcome to main"}
