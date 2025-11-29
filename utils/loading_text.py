from utils.helpers import *
import time
import sys

def loading(text=" Loading", duration=2):
    """
    Loading text

    Args:
        str text: Teks untuk ditampilkan sebagai loading text
        int duration: Durasi loading text

    Returns:
        None
    
    Raises:
        None
    """
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for dots in range(1, 4):
            sys.stdout.write(f"\r{text}" + "." * dots + "  ")
            sys.stdout.flush()
            time.sleep(0.4)
    
    print(f"\r{text}... (Succeed!)")
    time.sleep(0.5)
    clear_screen()