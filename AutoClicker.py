import pyautogui
import keyboard

# když zmáčknu x kliká to, jen 10 cps - při spuštění více instancí rychlejší, poté limitace jen procesorem xd - můj
# rekord 157 cps

while True:
    if keyboard.is_pressed('x'):
        pyautogui.click(pyautogui.position())
        pyautogui.click(pyautogui.position())
        pyautogui.click(pyautogui.position())
        pyautogui.click(pyautogui.position())
        pyautogui.click(pyautogui.position())
        pyautogui.click(pyautogui.position())
