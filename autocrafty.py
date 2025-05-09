import pyautogui
import time
import random
import numpy as np
import sys
import logging

logging.basicConfig(level=logging.DEBUG)


def main():


    for t in range(5):
        logging.info(f'Starting in {5-t}s')
        time.sleep(1)


    try:

        while True:

            pyautogui.press("num 0")
            time.sleep(3)
            pyautogui.press("num 0")
            time.sleep(3)
            pyautogui.press("v")
            time.sleep(40)



    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
