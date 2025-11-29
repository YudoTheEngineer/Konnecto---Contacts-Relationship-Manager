from utils.alerts import *

def create_form():
    while True:
        print("=======================================")
        print("| Konnecto - Contact Relationship APP |")
        print("=======================================")
        first_name = input(" First Name (required): ")
        
        if first_name:
            middle_name = input(" Middle Name: ")
            last_name = input(" Last Name: ")

            phone_number = input(" Phone Number: ")
            email = input(" Email Address: ")
            company = input(" Company: ")
            position = input(" Position: ")
            address = input(" Address: ")
            birth_date = input(" Birth Date (mm/yy/dd): ")
            note = input(" Note: ")
            social_media = input(" Social Media (LinkedIn - @YudoTheEngineer): ")
            category = input(" Category: ").lower()
            favourite = input(" Favourite (yes or no): ")

            if favourite.lower() == "yes":
                favourite = True
            
            elif favourite.lower() == "no" or favourite == "" :
                favourite = False
            
            else:
                yes_no_alert()

            return first_name, middle_name, last_name, phone_number, email, company, position, address, birth_date, note, social_media, category, favourite

        else:
            blank_input_alert()