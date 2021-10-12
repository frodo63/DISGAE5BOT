import pydirectinput
from pydirectinput import moveTo
from pydirectinput import press
#from pydirectinput import click

#from time import time
from time import sleep


def press_print(btn, name):
    print('pressed ' + str(btn) + ' - ' + name)
    press(btn)


pydirectinput.PAUSE = 1
pydirectinput.FAILSAFE = True



