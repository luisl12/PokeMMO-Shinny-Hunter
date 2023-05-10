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

def press_key(key):
    print('Pressing ' + key)
    time.sleep(1)
    pydirectinput.keyDown(key)
    time.sleep(.05)
    pydirectinput.keyUp(key)

def is_shinny(tesseract_path):
    # take screenshot
    image = pyautogui.screenshot()
    
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
        print('Shinny not found')
        return False

def reverse_steps(steps, new_steps=[]):
    if len(steps) < 1:
        raise Exception('Steps list must be filled')
    reverse = steps[::-1]
    reverse = [s for s in reverse if s != 'z']
    for i, e in enumerate(reverse):
        if e == 'right':
            reverse[i] = 'left'
        if e == 'left':
            reverse[i] = 'right'
        if e == 'up':
            reverse[i] = 'down'
        if e == 'down':
            reverse[i] = 'up'
    reverse.extend(new_steps)
    return reverse

def shinny_magikarp(path_to_tesseract, steps=[], sweet_scent_key='7', ava_sweet_scent=4, n_sweet_scent=4):
    """Find shinny magikarp with sweet scent and without leppa berries
    Always start from the location where magikarp is found.
    Make sure you use a pokemon with the Run Away ability to always escape from battle.

    Args:
        path_to_tesseract (string): Path to tesseract
        steps (list): List of strings with the keyboard presses
        sweet_scent_key (string): Sweet scent hotkey
        ava_sweet_scent (int): Number of sweet scent moves available
        n_sweet_scent (int): Number of sweet scent moves 
    """

    # TODO: Movement times can be better calibrated to make the hunting faster
    # TODO: What if we cant find the 'RUN' button ?

    print('Sweet scent available:', ava_sweet_scent)
    if ava_sweet_scent > 0:
        # start with the catch
        press_key(sweet_scent_key)
        # sleep enough to make the run button appear
        time.sleep(12)
        # find shinny
        found = is_shinny(path_to_tesseract)
        if not found:
            # run from battle
            try:
                x, y = pyautogui.locateCenterOnScreen('imgs/RUN.png', confidence=0.80)
            except TypeError:
                raise Exception("Cant find RUN button")
            pyautogui.click(x, y)

            # sleep a little to leave battle
            time.sleep(1.4)
            # repeat until we find shinny or sweet scent is out
            shinny_magikarp(path_to_tesseract, steps, sweet_scent_key, ava_sweet_scent-1)
        else:
            print("Shinny found GG EZ")
    else:
        print('Go to PC to reset sweet scent')
        # go to PC
        for step in steps:
            press_key(step)
        reversed_steps = reverse_steps(steps, new_steps=['z', 'z', 'z'])
        for step in reversed_steps:
            press_key(step)
        # repeat with sweet scent reset
        shinny_magikarp(path_to_tesseract, steps, sweet_scent_key, ava_sweet_scent=n_sweet_scent)
        

if __name__ == "__main__":

    time.sleep(2)
    path_to_tesseract = r"D:\Programas\Tesseract-OCR\tesseract.exe"
    steps = [
        'right','right', 'right', 'right', 'up', 'up', 'up', 
        'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'z', 
        'z', 'z', 'z', 'z', 'z', 'z', 'z'
    ]
    shinny_magikarp(path_to_tesseract, steps=steps, ava_sweet_scent=0, n_sweet_scent=4)