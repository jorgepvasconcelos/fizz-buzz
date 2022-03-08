from flask import Flask, request

from fizzbuzz_resolver import fizzbuzz_resolver
from validation import validation_fizzbuzz_route
from database.helpers import create_session
from database.models import User

app = Flask(__name__)


@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzz():
    data = request.get_json()

    validation = validation_fizzbuzz_route(data=data)
    if validation['error']:
        return validation['message_response'], validation['status_code']

    return {'result': fizzbuzz_resolver(value=data['value'])}


@app.route('/', methods=['GET'])
def index():
    return 'I am alive'


@app.route('/users', methods=['GET'])
def users():
    with create_session() as session:
        config = {'age': '10'}
        print(config)
        results = session.query(User).all()
        print(results)

    return 'I am alive'


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
