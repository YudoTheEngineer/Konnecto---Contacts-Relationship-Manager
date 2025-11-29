import time

def timer():
    """
    Timer 2.5 detik

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    time.sleep(2.5)

def clear_screen():
    """
    Membersihkan tampilan terminal

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    print("\033c",end="")