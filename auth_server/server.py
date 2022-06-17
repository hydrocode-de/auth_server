from typing import Callable
from flask import Flask, jsonify, request
from flask_cors import CORS
from auth_server import auth

app = Flask(__name__)
CORS(app, origin='*')


def _get_data() -> dict:
    # get the JSON body
    data = request.get_json()
    if data is None:
        data = {}

    # update with form data
    data.update(request.form)

    # add a Bearer token if any
    token = request.headers.get('Authorization')
    if token is not None:
        data['token'] = token.split(' ')[1]

    return data


def _run_api_func(func: Callable):
    # get data
    data = _get_data()

    # call the auth API
    try:
        response = func(**data)
    except Exception as e:
        return {'error': True, 'message': str(e)}
    
    # return userdata
    return response


@app.route('/register', methods=['POST'])
def register():
    # invoke API
    userdata = _run_api_func(auth.register)
    
    # return userdata
    if 'error' in userdata:
        return jsonify(userdata), 401
    return jsonify(userdata), 201


@app.route('/login', methods=['POST'])
def login():
    # invoke API
    userdata = _run_api_func(auth.login)

    # return userdata
    if 'error' in userdata:
        return jsonify(userdata), 401
    return jsonify(userdata), 200


@app.route('/verify', methods=['GET', 'POST'])
def verify_token():
    # invoke API
    userdata = _run_api_func(auth.verify_token)

    # return userdata
    if 'error' in userdata:
        return jsonify(userdata), 403
    return jsonify(userdata), 200


@app.route('/refresh', methods=['GET', 'POST'])
def refresh_token():
    # invoke API
    userdata = _run_api_func(auth.refresh_token)

    # return userdata
    if 'error' in userdata:
        return jsonify(userdata), 403
    return jsonify(userdata), 200


def run(host='localhost', port=5000, debug=False):
    app.run(host=host, port=port, debug=debug)


if __name__=='__main__':
    import fire
    fire.Fire(run)
