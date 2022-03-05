from flask import Flask, request
from fizz_buzz.fizz_buzz_resolver import fizz_buzz_resolver

app = Flask(__name__)


@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzz():
    data = request.get_json()
    value = data['value']

    if not value:
        return {'warning': 'you need send a "value" param'}, 400

    if not isinstance(value, int):
        return {'ValueError': 'value param must be a integer'}

    return {'result': fizz_buzz_resolver(value)}


if __name__ == '__main__':
    app.run(debug=True)
