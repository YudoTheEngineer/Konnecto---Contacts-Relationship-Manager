from .helpers import *

def value_error_alert():
    """ 
    Alert jika terjadi Value Error.
    
    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    print(" You need to input number in this field. ")
    clear_screen()
    timer()

def wrong_choice_alert():
    """ 
    Alert jika terjadi Wrong Choice saat memilih pilihan pada menu.
    
    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    print(" Wrong choice mate. ")
    clear_screen()
    timer()

def blank_input_alert():
    """ 
    Alert jika terjadi Blank Input.
    
    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    print(" You forgot to type something ")
    clear_screen()
    timer()

def yes_no_alert():
    """ 
    Alert jika menginputkan, inputan lain selain yes atau no di pilihan yang membutuhkan input tersebut.
    
    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """
    print(" It's a yes or no question. ")
    clear_screen()
    timer()