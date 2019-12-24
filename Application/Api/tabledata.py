from flask_restful import Resource


class TableData(Resource):
    def get(self):
        tabledata=[{ 'id': 1, 'name': 'Wasif', 'age': 21, 'email': 'wasif@email.com' },
      { 'id': 2, 'name': 'Ali', 'age': 19, 'email': 'ali@email.com' },
      { 'id': 3, 'name': 'Saad', 'age': 16, 'email': 'saad@email.com' },
      { 'id': 4, 'name': 'Asad', 'age': 25, 'email': 'asad@email.com' }]


        data = {"status": True,
                "message": "Logged in successfully",
                "tabledata":tabledata
                }
        return data, 200
