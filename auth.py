"""
Authentication module for Matrix Calculator
Handles user registration, login, and password hashing with salt
"""

import json
import bcrypt
import os
import re
from pathlib import Path

USERS_DB_PATH = Path(__file__).parent / "users_db.json"
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 50
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 50


def load_users_db():
    """Load users database from JSON file."""
    if USERS_DB_PATH.exists():
        with open(USERS_DB_PATH, 'r') as f:
            return json.load(f)
    return {}


def save_users_db(users_db):
    """Save users database to JSON file."""
    with open(USERS_DB_PATH, 'w') as f:
        json.dump(users_db, f, indent=2)


def validate_password(password: str) -> tuple[bool, str]:
    """
    Validate password strength.
    Requirements:
    - Length between 8 and 50 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters long"
    
    if len(password) > MAX_PASSWORD_LENGTH:
        return False, f"Password must not exceed {MAX_PASSWORD_LENGTH} characters"
    
    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"
    
    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"
    
    if not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password):
        return False, "Password must contain at least one special character (!@#$%^&*()-_=+[]{}|;:,.<>?/)"
    
    return True, ""


def validate_username(username: str) -> tuple[bool, str]:
    """
    Validate username.
    Requirements:
    - Length between 3 and 50 characters
    - Alphanumeric and underscore only
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if len(username) < MIN_USERNAME_LENGTH:
        return False, f"Username must be at least {MIN_USERNAME_LENGTH} characters long"
    
    if len(username) > MAX_USERNAME_LENGTH:
        return False, f"Username must not exceed {MAX_USERNAME_LENGTH} characters"
    
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    
    return True, ""


def hash_password(password: str) -> str:
    """Hash password with salt using bcrypt."""
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hashed version."""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except Exception:
        return False


def register_user(username: str, password: str) -> tuple[bool, str]:
    """
    Register a new user.
    
    Returns:
        tuple: (success, message)
    """
    # Validate username
    is_valid, error_msg = validate_username(username)
    if not is_valid:
        return False, error_msg
    
    # Validate password
    is_valid, error_msg = validate_password(password)
    if not is_valid:
        return False, error_msg
    
    users_db = load_users_db()
    
    # Check if user already exists
    if username in users_db:
        return False, "Username already exists"
    
    # Hash password and save user
    hashed_password = hash_password(password)
    users_db[username] = {
        "password": hashed_password,
        "matrices": []
    }
    
    save_users_db(users_db)
    return True, "User registered successfully"


def login_user(username: str, password: str) -> tuple[bool, str]:
    """
    Login user.
    
    Returns:
        tuple: (success, message)
    """
    users_db = load_users_db()
    
    if username not in users_db:
        return False, "Invalid username or password"
    
    user_data = users_db[username]
    
    if not verify_password(password, user_data["password"]):
        return False, "Invalid username or password"
    
    return True, "Login successful"


def user_exists(username: str) -> bool:
    """Check if user exists."""
    users_db = load_users_db()
    return username in users_db


def get_user_matrices(username: str) -> list:
    """Get user's matrices."""
    users_db = load_users_db()
    if username in users_db:
        return users_db[username].get("matrices", [])
    return []


def save_user_matrices(username: str, matrices: list) -> bool:
    """Save user's matrices."""
    users_db = load_users_db()
    if username in users_db:
        users_db[username]["matrices"] = matrices
        save_users_db(users_db)
        return True
    return False
