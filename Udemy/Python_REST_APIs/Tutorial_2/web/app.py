from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)
api = Api(app)

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('ThisIsNotAPassword')
client = MongoClient('mongodb://%s:%s@mongo:27017' % (username, password))
db = client.aNewDB
UserNum = db['UserNum']

UserNum.insert({
    'num_of_users': 0
})


class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {'$set': {'num_of_users': new_num}})
        return str('Hello User ' + str(new_num))


"""
* GET - gets something from the server
* POST - give data to the server to create something
* PUT - give data to the server to update something
* DELETE - alerts the server to delete something

Note: Need to rewrite to reuse code and to validate all input
"""

def check_posted_data(postedData, functionName):
    if (functionName in ['add', 'subtract', 'multiply']):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    elif (functionName == 'divide'):
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        elif int(postedData['y']) == 0: 
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, 'add')
        if (status_code != 200):
            retJson = {
                'message': 'An error happened',
                'status_code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x + y
        retMap = {
            'message': ret,
            'status_code': status_code
        }

        # Step 3: return the sum
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, 'subtract')
        if (status_code != 200):
            retJson = {
                'message': 'An error happened',
                'status_code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Subtract the posted data
        ret = x - y
        retMap = {
            'message': ret,
            'status_code': status_code
        }

        # Step 3: return the sum
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, 'multiply')
        if (status_code != 200):
            retJson = {
                'message': 'An error happened',
                'status_code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Multiply the posted data
        ret = x * y
        retMap = {
            'message': ret,
            'status_code': status_code
        }

        # Step 3: return the sum
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        # Step 1: Get posted data
        postedData = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(postedData, 'divide')
        if (status_code != 200):
            retJson = {
                'message': 'An error happened',
                'status_code': status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)

        # Step 2: Divide the posted data
        ret = float(x / y)
        retMap = {
            'message': ret,
            'status_code': status_code
        }

        # Step 3: return the sum
        return jsonify(retMap)


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/sub')
api.add_resource(Multiply, '/mul')
api.add_resource(Divide, '/div')
api.add_resource(Visit, '/hello')


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
