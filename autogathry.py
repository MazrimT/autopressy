import pyautogui
import time
import random
import numpy as np
import sys
import logging
import toml

logging.basicConfig(level=logging.DEBUG)

def wait():
    time.sleep(random.choice(np.arange(2, 3, 0.1)))


def main():



    for t in range(5):
        logging.info(f'Starting in {5-t}s')
        time.sleep(1)

    with open('config.toml', 'r') as f:
        config = toml.load(f)

    keybind = config.get('keybind')
    adjust_camera = config.get('adjust_camera')

    if not keybind:
        sys.exit(1)

    if adjust_camera:

        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('up')
        time.sleep(5)
        pyautogui.keyUp('up')
        pyautogui.keyUp('ctrl')

    try:

        while True:

            pyautogui.press(keybind)
            wait()
            pyautogui.press('num0')
            wait()
            pyautogui.keyDown('right')
            time.sleep(0.1)
            pyautogui.keyUp('right')

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
