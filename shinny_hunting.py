# -*- coding: utf-8 -*-
"""
ShinnyHunter.shinny_hunting
-----------------

This module runs shinny hunter bot.
"""

# imports
import time
import pydirectinput
import pyautogui
from pytesseract import pytesseract


def press_up():
    print('PRESSING UP...')
    time.sleep(1)
    pydirectinput.keyDown('up')
    time.sleep(.05)
    pydirectinput.keyUp('up')

def press_down():
    print('PRESSING DOWN...')
    time.sleep(1)
    pydirectinput.keyDown('down')
    time.sleep(.05)
    pydirectinput.keyUp('down')

def press_left():
    print('PRESSING LEFT...')
    time.sleep(1)
    pydirectinput.keyDown('left')
    time.sleep(.05)
    pydirectinput.keyUp('left')

def press_right():
    print('PRESSING RIGHT...')
    time.sleep(1)
    pydirectinput.keyDown('right')
    time.sleep(.05)
    pydirectinput.keyUp('right')

def is_shinny(tesseract_path):
    # take screenshot
    image = pyautogui.screenshot()

    # debug screenshot
    image.show()
    
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = tesseract_path
    
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(image)
    
    # Displaying the extracted text
    words = text[:-1]

    # return clause
    if words.find('Shinny') >= 0:
        print('Shinny found')
        return True
    else:
        print("Shinny not found")
        return False

def shinny_magikarp(path_to_tesseract, n_steps=0, trip=[], sweet_scent_key='7', n_sweet_scent=4):
    """Find shinny magikarp with sweet scent and without leppa berries
    Always start from the location where magikarp is found

    Args:
        path_to_tesseract (string): Path to tesseract
        n_steps (int): Number of steps taken to move from the location to PC
        trip (list): List of strings with the keyboard presses
        sweet_scent_key (string): Sweet scent hotkey
        n_sweet_scent (int): Number of sweet scent moves available
    """

    if n_sweet_scent > 0:
        # start with the catch
        pydirectinput.keyDown(sweet_scent_key)
        # sleep enough to make the run button appear
        time.sleep(12)
        # find shinny
        found = is_shinny(path_to_tesseract)
        if not found:
            # TODO Run from battle and sleep a little
            print("")
            # shinny_magikarp(path_to_tesseract, n_steps-1, trip, sweet_scent_key, n_sweet_scent-1)
    else:
        print("Go to PC!!!")

if __name__ == "__main__":

    time.sleep(2)
    path_to_tesseract = r"D:\Programas\Tesseract-OCR\tesseract.exe"
    shinny_magikarp(path_to_tesseract, n_sweet_scent=3)