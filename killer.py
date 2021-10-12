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
#y = 1
#while y <3:
x = 1
while x <= 1000:
    pydirectinput.PAUSE = 0.5
    moveTo(1400, 900)  # на тайл
    sleep(0.5)
    press_print('k', 'имя карты')#имя карты
    pydirectinput.PAUSE = 1.2
    press_print('k','да в диалоге')#да в диалоге
    pydirectinput.PAUSE = 0.4
    press_print('k','на дебаф')#на дебаф
    press_print('k','на панель')#на пaнель
    press_print('k','выбираем Киллиа')#выбираем Киллиа
    press_print('k','выбираем MOVE')#выбираем MOVE
    moveTo(600, 240)#на тайл
    press_print('k','подтвердить движение')#подтвердить движение
    press_print('4','special')  # special
    press_print('k','cap2 select')  # cap2 select
    press_print('k','cap2 confirm')  # cap2 confirm
    pydirectinput.PAUSE = 1.5
    press_print('2','end turn')  # end turn
    #press_print('esc','3 captured')#3 captured
    press_print('k','награды')#награды
    pydirectinput.PAUSE = 0.1
    press_print('k','экспа')#экспа
    x+=1
    press_print('k', 'просто')  # награды
    press_print('k', 'закрыть')  # награды
    pydirectinput.PAUSE = 1
    press_print('esc', 'так')  # награды

