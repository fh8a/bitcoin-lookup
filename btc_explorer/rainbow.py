import sys
import time
import colorsys
from colorama import init

init() 

def hsv_to_rgb(h, s=1.0, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

def print_rainbow(text, delay=0.01):
    for i, char in enumerate(text):
        hue = i / len(text)  # from 0 to 1
        r, g, b = hsv_to_rgb(hue)
        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line
