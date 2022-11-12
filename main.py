from src.layers.presentation.display import display_sort_stack, display_txt_files
from time import sleep
import pyautogui

pyautogui.hotkey("win", "r")
sleep(1)
pyautogui.write("cmd", interval=0.1)
pyautogui.press("enter")
sleep(1)
pyautogui.write(
    "cd Desktop\\Algorithms\\Projects\\automation_project", interval=0.1)
sleep(2)
pyautogui.press("enter")
pyautogui.write(
    "start %windir%\explorer.exe " "C:\\Users\\fx403\\Desktop\\Algorithms\\Projects\\Test")
pyautogui.press("enter")

#* Show the .txt files
display_txt_files()

print()

#* Show the stack created
display_sort_stack()
        
