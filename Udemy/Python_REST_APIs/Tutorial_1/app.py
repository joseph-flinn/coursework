from flask import Flask, jsonify, request

app = Flask(__name__) # __name__ is just a convention

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hithere')
def hi_there_everyone():
    return 'I just hit /hithere'

@app.route('/bye')
def bye():
    # return can take a string, json, or page
    retJson = {
        'Name': 'Flinn',
        'Age': 24,
        'phones': [
            {
                'phoneName': 'iPhone',
                'phoneNumber': '111-111-1111'
            },
            {
                'phoneName': 'Pixel',
                'phoneNumber': '222-222-2222'
            }
        
        ]
    }
    return jsonify(retJson)

@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    """
    Assumes that the user is sending valid x and y. This is a bad assumption. 
    Never trust the user.
    """
    # get x, y from posted data
    dataDict = request.get_json()
    # Example of a simple check
    if "y" not in dataDict or "x" not in dataDict:
        return "ERROR", 305
    x = dataDict['x']
    y = dataDict['y']

    # add z = x + y
    z = x + y

    # prepare a JSON, 'z': z
    retJson = {
        'z': z
    }

    # return json
    return (jsonify(retJson), 200)


if __name__ == '__main__':
    app.run(debug=True)
