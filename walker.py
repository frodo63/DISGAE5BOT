
from pydirectinput import moveTo
from pydirectinput import press
from pydirectinput import click
from pydirectinput import keyDown
from pydirectinput import keyUp
from pydirectinput import mouseDown
from pydirectinput import mouseUp

from mss import mss

from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_loop

#from time import time
from time import sleep


def press_print(btn, name):
    print('pressed ' + str(btn) + ' - ' + name)
    press(btn)

def mouse_move(say, path_pic):
    pos = imagesearch_loop('path_pics/'+path_pic, 1)
    if pos[0] != -1:
        mouseDown(pos[0], pos[1])
        sleep(0.1)
        mouseUp(pos[0], pos[1])
        print(say+' - position : ', pos[0], pos[1])
    else:
        print("image not found")





#pydirectinput.PAUSE = 1



sleep(3)
#клик мышкой
mouse_move('1','path_1.png')
sleep(2)
mouse_move('2','path_2.png')
sleep(2)
mouse_move('3','path_3.png')
sleep(2)
mouse_move('4','path_4.png')
sleep(2)
mouse_move('5','path_5.png')
sleep(2)
mouse_move('6','path_6.png')
sleep(2)
mouse_move('7','path_7.png')
sleep(2)
keyDown('w')
keyDown('d')
sleep(0.3)
press('k')
press('k')

press('k')

#начали пытать
press('k')
sleep(1)
press('k')
sleep(1)

press('k')
sleep(1)
press('k')
sleep(1)

press('k')
sleep(1)
press('k')
sleep(1)

press('k')
sleep(1)
press('k')
sleep(1)

press('k')
sleep(1)
press('k')
sleep(1)

press('l')
sleep(1)

#надо екстрактнуть
click(420, 537, 1)
press('k')

sleep(1)

press('j')
sleep(1)
press('k')
sleep(1)
press('k')
sleep(1)
press('l')
sleep(1)
press('l')






