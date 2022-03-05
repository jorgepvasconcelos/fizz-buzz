from flask import Flask, request
from fizz_buzz.fizz_buzz_resolver import fizz_buzz_resolver
from validation import validation_fizzbuzz_route

app = Flask(__name__)


@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzz():
    data = request.get_json()

    validation = validation_fizzbuzz_route(data=data)
    if validation['error']:
        return validation['message_response'], validation['status_code']

    value = data['value']
    return {'result': fizz_buzz_resolver(value)}


if __name__ == '__main__':
    app.run(debug=True)
