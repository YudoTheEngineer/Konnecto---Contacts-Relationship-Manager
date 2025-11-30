from utils.alerts import *
from utils.loading_text import loading
import json

def contacts_list(JSON_PATH):
    while True:
        try:
            with open(JSON_PATH, "r", encoding="utf-8") as file:
                contacts = json.load(file)

        except FileNotFoundError:
            file_not_found_alert()

        except json.JSONDecodeError:
            decode_error_alert()

        if not contacts:
            no_contact_alert()
            return

        print("=======================================")
        print("| Konnecto - Contact Relationship APP |")
        print("|             All Contact             |")
        print("=======================================")

        for i, contact in enumerate(contacts, start=1):
            full_name = contact.get("full_name")
            
            print(f"{i:2}. {full_name}")
        
        print("=======================================")

        try:
            update_choice = int(input(" Enter the contact number to do update (0 to go back): "))

            if update_choice == 0:
                return

            if update_choice <= len(contacts):
                selected_contact = contacts[update_choice - 1]
                clear_screen()

            else:
                wrong_choice_alert()

        except ValueError:
            value_error_alert()