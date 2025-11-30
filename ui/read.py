from utils.alerts import *
from utils.loading_text import loading
import json

def read_contacts(JSON_PATH):
    loading(" Loading all contacts in database")

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
            read_choice = int(input(f" Enter the contact number to view details (0 to go back): "))

            if read_choice == 0:
                loading(" Back to Main Menu", 1)
                return
            
            if read_choice <= len(contacts):
                selected_contact = contacts[read_choice - 1]
                clear_screen()

                print("=======================================")
                print("| Konnecto - Contact Relationship APP |")
                print("|             All Contact             |")
                print("=======================================")
                print(f" Name: {selected_contact.get("full_name")}")
                print(f" Phone Number: {selected_contact.get("phone_number")}")
                print(f" Email Address: {selected_contact.get("email")}")
                print(f" Company: {selected_contact.get("company")}")
                print(f" Position: {selected_contact.get("position")}")
                print(f" Address: {selected_contact.get("address")}")
                print(f" Birthdate: {selected_contact.get("birth_date")}")
                print(f" Note: {selected_contact.get("note")}")
                print(f" Social Media: {selected_contact.get("social_media")}")
                print(f" Category: {selected_contact.get("category")}")
                print(f" Favourite: {selected_contact.get("favourite")}")

                input(" Enter to go back: ")
                loading(" Back to Main Menu", 1)
                return

            else:
                wrong_choice_alert()
                
        except ValueError:
            value_error_alert()