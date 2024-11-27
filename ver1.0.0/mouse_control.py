# mouse_control.py
import pyautogui

def move_mouse(x, y):
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(x * screen_width, y * screen_height)

def click_mouse(button='left'):
    pyautogui.click(button=button)
