# pip install pyautogui

import pyautogui
import time

def clickmouse(x=457,y=533,loop=10,clicks=10,sleep=0.1):
    t1 = time.time()
    pyautogui.moveTo(x,y)
    for i in range(loop):
            pyautogui.click(clicks=clicks)
            time.sleep(sleep)
    t2 = time.time()
    print('Time: ',t2-t1)


clickmouse()
