import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="p")

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)
        
def toggle(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
        
clicker_thread = threading.Thread(target=clicker)
clicker_thread.start()
with Listener(on_press=toggle) as listener:
    listener.join()