from flask import Flask, request
from fizz_buzz.fizzbuzz_resolver import fizzbuzz_resolver
from validation import validation_fizzbuzz_route

app = Flask(__name__)


@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzz():
    data = request.get_json()

    validation = validation_fizzbuzz_route(data=data)
    if validation['error']:
        return validation['message_response'], validation['status_code']

    return {'result': fizzbuzz_resolver(value=data['value'])}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
