# task_04_flask.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store of users; keys are usernames
users = {}

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data', methods=['GET'])
def get_usernames():
    """
    Return a JSON list of all usernames currently in `users`.
    E.g. [] or ["jane", "john"]
    """
    # list(users.keys()) will be [] until you add users via /add_user
    return jsonify(list(users.keys())), 200

# Example of add_user so you can actually populate users:
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json() or {}
    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Prevent overwriting
    if username in users:
        return jsonify({'error': 'User already exists'}), 400

    users[username] = {
        'username': username,
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    return jsonify({
        'message': 'User added',
        'user': users[username]
    }), 201

if __name__ == '__main__':
    app.run()
