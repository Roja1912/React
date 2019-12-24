from flask_restful import Resource
from flask_restful import reqparse
from Application.Model.models import UserModel

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
                            help='This field cannot be blank',
                            required=True)
        parser.add_argument('password',
                            help='This field cannot be blank',
                            required=True)
        user_data = parser.parse_args()
        user = UserModel(username=user_data['username'],
                         password=user_data['password'],
                    )
        user.save_to_db()
        data = {"status": True,
                "message": "Logged in successfully",
                }
        return data, 200




