from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
db_users = {}

@app.route('/')
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data')
def list_usernames():
    """Returns a JSON list of all usernames."""
    return jsonify(list(db_users.keys()))

@app.route('/status')
def status():
    """Returns plain text OK to indicate service health."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Returns the user object for the given username or 404 if not found."""
    user = db_users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the in-memory store."""
    payload = request.get_json()
    # Check for JSON and required field
    if not payload or 'username' not in payload:
        return jsonify({"error": "Username is required"}), 400
    username = payload['username']
    # Build user object
    user = {
        "username": username,
        "name": payload.get('name'),
        "age": payload.get('age'),
        "city": payload.get('city')
    }
    db_users[username] = user
    return jsonify({"message": "User added", "user": user}), 201

if __name__ == '__main__':
    app.run()
