import os
import numpy as np
from scipy.ndimage import zoom
import random
from colorama import init, Fore, Style

# Initialiser colorama pour le terminal
init(autoreset=True)

# Liste de couleurs ANSI de colorama
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def mask_to_ascii(mask, cols=100, fg_chars='0123456789', bg_char='.'):
    h, w = mask.shape

    scale_x = cols / w
    scale_y = scale_x * 0.5  # Ajustement du ratio terminal

    resized = zoom(mask.astype(float), (scale_y, scale_x), order=0) > 0.5

    ascii_art = ""
    for row in resized:
        line_chars = []
        for pixel in row:
            if pixel:
                digit = random.choice(fg_chars)
                color = random.choice(colors)
                line_chars.append(color + digit + Style.RESET_ALL)
            else:
                line_chars.append(bg_char)
        ascii_art += "".join(line_chars) + "\n"
    return ascii_art

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
