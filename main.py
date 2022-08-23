from multiprocessing.connection import wait
import pyautogui
import time
import keyboard
import math
from random import random


# https://stackoverflow.com/questions/23700822/weighted-random-coordinates
def randomPoint(aroundX, aroundY, scale=1, density=2):
    angle = random()*2*math.pi

    x = random()
    if x == 0:
        x = 0.0000001

    distance = scale * (pow(x, -1.0/density) - 1)
    return (aroundX + distance * math.sin(angle),
            aroundY + distance * math.cos(angle))


def random_weighted_click(aroundX, aroundY):
    x, y = randomPoint(aroundX, aroundY)
    pyautogui.click(x, y)


def random_weighted_click_pos(pos):
    point = pyautogui.center(pos)
    random_weighted_click(point[0], point[1])


def locate_image_on_screen(image_path):
    pos = pyautogui.locateOnScreen(
        image_path, grayscale=False, confidence=0.7)
    return pos


def check_bookmarks():
    mystic_pos = locate_image_on_screen("Pics\\mystic.png")
    coven_pos = locate_image_on_screen("Pics\\covenant.png")

    if mystic_pos:
        mystic_point = pyautogui.center(mystic_pos)
        random_weighted_click(mystic_point[0]+800, mystic_point[1]+50)

        time.sleep(0.5)

        buy_button_mystic_pos = locate_image_on_screen(
            "Pics\\Buy_button_Mystic.png")
        random_weighted_click_pos(buy_button_mystic_pos)

        global mystic
        mystic += 1
        time.sleep(1)

    if coven_pos:
        coven_point = pyautogui.center(coven_pos)
        random_weighted_click(coven_point[0]+800, coven_point[1]+50)

        time.sleep(0.5)

        buy_button_covenant_pos = locate_image_on_screen(
            "Pics\\Buy_button_Covenant.png")
        random_weighted_click_pos(buy_button_covenant_pos)

        global covenant
        covenant += 1
        time.sleep(1)


def scroll():
    x, y = randomPoint(1263, 590)
    pyautogui.moveTo(x, y)

    z, w = randomPoint(-350, 0.5)
    pyautogui.drag(0, z, 0.5, button="left")


def check_store():
    check_bookmarks()
    scroll()
    check_bookmarks()


def refresh(error_counter=0):
    try:
        refresh_button_pos = locate_image_on_screen("Pics\\refresh_button.png")
        random_weighted_click_pos(refresh_button_pos)

        time.sleep(1)

        confirm_pos = locate_image_on_screen("Pics\\confirm button.png")
        random_weighted_click_pos(confirm_pos)

        global refreshes
        refreshes += 1

        time.sleep(1)
    except:
        if error_counter < 3:
            refresh(error_counter + 1)
        else:
            raise Exception(
                "Will not try to refresh again, have tried 3 times")


mystic, refreshes, covenant = 0, 0, 0


def show_stats():
    print("Total Covenant: ", covenant)
    print("Total Mystic: ", mystic)
    print("Total Refreshes: ", refreshes)


def main():
    try:
        print("Waiting for you to focus on the Epic 7...")
        time.sleep(5)
        while keyboard.is_pressed('q') == False:
            print("Total Covenant: ", covenant)
            check_store()
            refresh()
    except KeyboardInterrupt:
        print('ctrl+c interrupted')
    show_stats()


if __name__ == '__main__':
    main()
