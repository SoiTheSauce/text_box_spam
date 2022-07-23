import pyautogui
import time

time.sleep(10)
#pauses the code for 10s for you to change the cursor to the place you want to spam
while True:
    pyautogui.typewrite('any input')
    #type anything here
    time.sleep(1)
    # a pause to prevent the code form lagging out the pc
    pyautogui.press('enter')
    #key to be pressed
    pyautogui.typewrite('fany input')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.typewrite('any input')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(40)