from utils.alerts import *

def main_menu():
    """
    Konnecto Main Menu

    Args:
        None

    Returns:
        Int menu_choice: Pilihan pengguna pada bagian menu

    Raises:
        ValueError: Jika menu_choice tidak diisi dan atau menu_choice diisi selain angka
    """

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
            return menu_choice

        else:
            wrong_choice_alert()

    except ValueError:
        value_error_alert()