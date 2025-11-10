"""
common.py
Common utility functions used by both faculty and student modules.
"""

import json
import os
import random
import string

DATA_FILE = "data.json"


def load_data():
    """Load JSON data file or create a new one if not exists."""
    if not os.path.exists(DATA_FILE):
        return {"faculties": {}, "students": {}, "classes": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """Save current data dictionary to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def generate_username(prefix="stu"):
    """Generate random username like stu_ab12x3."""
    return f"{prefix}_{''.join(random.choices(string.ascii_lowercase+string.digits, k=6))}"


def generate_password(length=8):
    """Generate a random password with letters + digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
