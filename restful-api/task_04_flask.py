# task_04_flask.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store of user objects, keyed by username
users = {}


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Flask API!', 200


@app.route('/data', methods=['GET'])
def get_usernames():
    """
    Return a JSON list of all usernames currently in `users`.
    E.g. [] or ["jane", "john"]
    """
    return jsonify(list(users.keys())), 200


@app.route('/status', methods=['GET'])
def status():
    return 'OK', 200


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Return the full user object for the given username,
    or a 404 error if not found.
    """
    user = users.get(username)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the in-memory store.
    Expected JSON payload:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    """
    if not request.is_json:
        return jsonify({'error': 'JSON body required'}), 400

    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    if username in users:
        return jsonify({'error': 'User already exists'}), 400

    # Build and store the user object
    user_obj = {
        'username': username,
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[username] = user_obj

    return jsonify({
        'message': 'User added',
        'user': user_obj
    }), 201


if __name__ == '__main__':
    app.run()
