from utils.alerts import *

def create_form():
    """
    Form untuk pengisian data objek yang akan di simpan

    Args:
        None

    Returns:
        string: 
            first_name: Nama depan objek
            middle_name: Nama tengah objek
            last_name: Nama belakang objek
            phone_number: Nomor telepon objek
            email: Email address objek
            company: Perusahaan Tempat bekerja objek
            position: Jabatan objek
            birth_date: Tanggal lahir objek
            note: Catatan tambahan untuk objek
            social_media: Media sosial objek
            category: Kategori objek
        
        boolean favourite: Apakah objek difavoritkan atau tidak

    Raise:
        None
    """
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