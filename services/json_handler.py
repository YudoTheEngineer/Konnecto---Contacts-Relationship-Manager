import json
import os

def init_database(JSON_PATH):
    folder = os.path.dirname(JSON_PATH)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, "w") as file:
            json.dump([], file)

def load_database(JSON_PATH):
    init_database(JSON_PATH)
    with open (JSON_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def save_to_database(JSON_PATH, contact_data):
    contacts = load_database(JSON_PATH)
    contacts.append(contact_data)
    with open(JSON_PATH, "w") as file:
        json.dump(contacts, file, indent=4)