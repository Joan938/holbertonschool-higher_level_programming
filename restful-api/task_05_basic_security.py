# task_05_basic_security.py

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt
)

app = Flask(__name__)

# ----- Basic Auth Setup -----
auth = HTTPBasicAuth()

# In-memory user store
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify Basic Auth credentials against the in-memory users dict.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# ----- JWT Setup -----
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # change this in production!
jwt = JWTManager(app)


@jwt.unauthorized_loader
def handle_missing_token(err_msg):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err_msg):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ----- Endpoints -----


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected by HTTP Basic Auth.
    """
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """
    Accepts JSON with 'username' and 'password'.
    Returns a JWT access token if valid.
    """
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad credentials"}), 401

    # Include role in token claims
    additional_claims = {"role": user["role"]}
    token = create_access_token(identity=username,
                                additional_claims=additional_claims)
    return jsonify({"access_token": token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected by JWT token.
    """
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Protected by JWT token + role check.
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run()
