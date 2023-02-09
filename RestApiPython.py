from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.get_json()

    if len(output.keys()) < 2:
        return {"Status": "BAD Response"}

    num1 = int(output['firstInput'])
    num2 = int(output['secInput'])

    cal = {}

    cal['addition'] = num1 + num2
    cal['subtraction'] = num1 - num2
    cal['multiplication'] = num1 * num2
    cal['division'] = num1 / num2
    cal['average'] = (num1 + num2) / 2

    return (cal)

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10

    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number": copy_n,
            'Armstrong': True,
            "Server ID": "122.234.213.53",
            "Other Numbers": [1,23,43,5,3]
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number": copy_n,
            'Armstrong': False,
            "Server ID": "122.234.213.53",
            "Other Numbers": [1,23,43,5,3]
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port = 2000)