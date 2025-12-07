
import json
import os
import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'ideas.json')

def _ensure_data_dir():
    """Ensures the data directory exists."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

def save_idea(title, description):
    """Saves a new prototype idea."""
    _ensure_data_dir()

    new_idea = {
        "timestamp": datetime.datetime.now().isoformat(),
        "title": title,
        "description": description
    }

    with open(DATA_FILE, 'r') as f:
        try:
            ideas = json.load(f)
        except json.JSONDecodeError:
            ideas = []

    ideas.append(new_idea)

    with open(DATA_FILE, 'w') as f:
        json.dump(ideas, f, indent=4)

    return True

def list_ideas():
    """Returns a list of all saved ideas."""
    _ensure_data_dir()

    with open(DATA_FILE, 'r') as f:
        try:
            ideas = json.load(f)
        except json.JSONDecodeError:
            ideas = []

    return ideas

def delete_idea(index):
    """Deletes an idea by index (0-based)."""
    _ensure_data_dir()

    with open(DATA_FILE, 'r') as f:
        ideas = json.load(f)

    if 0 <= index < len(ideas):
        deleted = ideas.pop(index)
        with open(DATA_FILE, 'w') as f:
            json.dump(ideas, f, indent=4)
        return deleted
    return None
