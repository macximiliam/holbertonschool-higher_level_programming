# task_05_basic_security.py
from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
import datetime
import os

app = Flask(__name__)

# ----------------------------
# Configuration
# ----------------------------
# Use a secret key for JWT signing. In production, load this from env vars or a secret manager.
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "change-this-secret-key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)

# Initialize JWT manager
jwt = JWTManager(app)

# Initialize HTTP Basic Auth
auth = HTTPBasicAuth()

# ----------------------------
# In-memory users store
# ----------------------------
# Users stored in-memory as required. Passwords are hashed using werkzeug.
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}

# ----------------------------
# Basic Auth verification
# ----------------------------
@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for HTTP Basic Auth.
    Returns True if credentials match, False otherwise.
    """
    if not username or not password:
        return False
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)

# Optional: return JSON 401 for Basic Auth failures (consistent error format)
@auth.error_handler
def basic_auth_error():
    """
    Return JSON 401 when basic auth fails or is missing.
    """
    return jsonify({"error": "Unauthorized access"}), 401

# ----------------------------
# JWT error handlers (ensure 401 for JWT auth problems)
# ----------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err_msg):
    """Missing or malformed token -> 401"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err_msg):
    """Invalid token -> 401"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Expired token -> 401"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Revoked token -> 401"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err_msg):
    """Fresh token required -> 401"""
    return jsonify({"error": "Fresh token required"}), 401

# ----------------------------
# Routes
# ----------------------------
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    A route protected by HTTP Basic Auth. Returns plain text on success.
    """
    # Successful basic auth should return the exact message required
    return make_response("Basic Auth: Access Granted", 200)

@app.route("/login", methods=["POST"])
def login():
    """
    Login route that returns a JWT access token when credentials are valid.
    Expects JSON: {"username": "...", "password": "..."}
    """
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 401

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        # Invalid credentials -> 401
        return jsonify({"error": "Bad username or password"}), 401

    # Include role in additional claims so we can check roles later
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify({"access_token": access_token}), 200

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    A route protected by JWT. Returns plain text on success.
    """
    # If JWT is valid, return exact required message
    return make_response("JWT Auth: Access Granted", 200)

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Route accessible only to users with role 'admin'.
    Returns 403 with JSON error if user is not admin.
    """
    claims = get_jwt()
    role = claims.get("role", None)
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return make_response("Admin Access: Granted", 200)

# ----------------------------
# Run the app (only when executed directly)
# ----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
