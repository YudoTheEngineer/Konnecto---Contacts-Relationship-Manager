from utils.alerts import *

def main_menu():
    print(""" 
=======================================
| Konnecto - Contact Relationship APP |
|   Contact CRUDS   |     Options     |
=======================================
| 1. Create         | 6. Category     |
| 2. Read           | 7. Favorite     |
| 3. Update         | 8. Interaction  |
| 4. Delete         | 9. Reminder     |
| 5. Search         | 10. Download    |
|===================| 11. Upload      |
| Created By Yudo A | 12. Exit        |
=======================================
    """)

    try:
        menu_choice = int(input(" Select (1 - 12): "))

        if menu_choice > 0 and menu_choice < 13:
            clear_screen()
            return menu_choice

        else:
            wrong_choice_alert()

    except ValueError:
        value_error_alert()