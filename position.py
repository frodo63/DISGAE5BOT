import os
import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE - True

print('Для выхода используйте <Ctrl+C>')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = '\b X : ' + str(x).rjust(4) + ' Y : ' + str(y).rjust(4)
        print(positionStr)
        #print('\b' * len(positionStr), end='', flush=True)

except:
    os.system('clear')
    print('программа завершена')
