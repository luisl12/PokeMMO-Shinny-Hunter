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

# testing keyboard press
# press_up()
# press_left()
# press_down()
# press_right()

# take screenshot
image = pyautogui.screenshot()

# image to text
path_to_tesseract = r"D:\Programas\Tesseract-OCR\tesseract.exe"

# area = (330, 155, 300 + 290, 100 + 100)
# image = image.crop(area)
image.show()
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(image)
  
# Displaying the extracted text
print(text[:-1])