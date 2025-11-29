# User Interfaces
from ui.main_menu import main_menu
from ui.create import create_form

# Models
from models.contact import Contact

# Services
from services.json_handler import *

# Utilities
from utils.helpers import *
from utils.alerts import *
from utils.loading_text import *

# JSON File Path
JSON_PATH = "database/contacts.json"
init_database(JSON_PATH)

# Main Loop
while True:

    # Main Menu
    menu_choice = main_menu()
    
    match (menu_choice):
        case 1:
            # Loading Text
            loading(" To Create Form")

            # Create New Contact Form
            first_name, middle_name, last_name, phone_number, email, company, position, address, birth_date, note, social_media, category, favourite = create_form()

            # Create New Object
            new_contact = Contact(first_name, middle_name, last_name, phone_number, email, company, position, address, birth_date, note, social_media, category, favourite)

            # Convert Object To Dictionary
            contact_data = new_contact.to_dict()

            # Save Dictionary To Database
            save_to_database(JSON_PATH, contact_data)

            # Loading Text
            loading(" Saving Contact")

        case 12:
            # Loading Text
            loading(" Closing Program And Bye - Bye")
            exit()