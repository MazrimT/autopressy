from pynput.keyboard import Key, Controller
from time import sleep
import random
import numpy as np
from logger import make_logger


def press_key(k, rand):

    if k == 's':
        rand = round(rand*3, 2)

    extra_sleep_list = np.arange(0.1, 2.1, 0.1)

    if pick_binary == 0:
        logger.info(f'pressing {k} for {rand} seconds')
    else:
        logger.info(f'pressing {k} for {rand} seconds with space')

    keyboard.press(k)

    if pick_binary == 1:
        sleep(0.4)
        keyboard.press(Key.space)
        sleep(0.1)
        keyboard.release(Key.space)

    sleep(rand+random.choice(extra_sleep_list)-0.5)

    keyboard.release(k)
    sleep(rand/10+1)


def press_arrow():

    d = random.choice(['left', 'right'])

    logger.info(f"pressing arrow {d}")

    if d == 'left':
        keyboard.press(Key.left)
        sleep(1)
        keyboard.release(Key.left)
    
    elif d == 'right':
        keyboard.press(Key.right)
        sleep(1)
        keyboard.release(Key.right)


def press_nine():


    if pick_binary == 1:
        logger.info("Using 9")
        keyboard.press('9')
        keyboard.release('9')

def start_msg():

    for r in reversed(range(5)):

        logger.info(f'Starting in {r}')
        sleep(1)

def pick_a_key():
    return random.choice([
            ['a', 'd'],
            ['d', 'a'],
            ['w', 's'],
            ['s', 'w']
    ])

def pick_binary():
    return random.randint(0,1)

def main():
    while True:

        #rand = random.randrange(1, 5)
        rand = round(random.choice(np.arange(1, 3, 0.1)), 2)

        # press 9, or dont
        press_nine()

        # press the arrows
        press_arrow()

        # do keys
        [press_key(k,rand) for k in pick_a_key()]

        actual_sleep = rand*30

        logger.info(f"sleeping for {actual_sleep} seconds")

        sleep(actual_sleep-5)

        for r in reversed(range(5)):
            logger.info(f"pressing in {r}")


if __name__ == '__main__':

    logger = make_logger()
    logger.info('Starting')





    keyboard = Controller()
    start_msg()
    main()
    
