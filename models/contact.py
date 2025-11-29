class Contact:
    def __init__(self, first_name:str, middle_name:str = "", last_name:str = "", phone_number:str = "", email:str = "", company:str = "", position:str = "", address:str = "", birth_date:str = "", note:str = "", social_media:str = "", category:str = "", favourite:bool = False ):
        # Name Data
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        # Full Name
        name_parts = [first_name, middle_name, last_name]
        self.full_name = " ".join(part for part in name_parts if part)

        # Contacts Data
        self.phone_number = phone_number
        self.email = email

        # Professional Data   
        self.company = company
        self.position = position
        self.address = address
        self.birth_date = birth_date
        self.note = note

        # More Information Data
        self.social_media = social_media
        self.category = category
        self.favourite = favourite

    def to_dict(self):
        contact = {
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "company": self.company,
            "position": self.position,
            "address": self.address,
            "birth_date": self.birth_date,
            "note": self.note,
            "social_media": self.social_media,
            "category": self.category,
            "favourite": self.favourite 
        }

        return contact