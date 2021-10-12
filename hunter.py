import pydirectinput
from pydirectinput import moveTo
from pydirectinput import press
from pydirectinput import click
from pydirectinput import keyDown
from pydirectinput import keyUp

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
while x <= 42:
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
    #тут неясно, какое сработает: k или click
    press_print('k','подтвердить движение')#подтвердить движение
    #click_print(330,157)#
    #press_print('k','')#это походу ненадо
    press_print('4','special')  # special
    press_print('k','cap2 select')  # cap2 select
    press_print('k','cap2 confirm')  # cap2 confirm
    press_print('2','end turn')  # end turn
    pydirectinput.PAUSE = 1
    press_print('k','3 captured')#3 captured
    press_print('k','награды')#награды
    pydirectinput.PAUSE = 0.5
    press_print('k','экспа')#экспа
    print('\b Цикл : ' + str(x) + ' из 42. Пленных примерно: ' + str(x*3))
    x+=1

    #ДОЙТИ ДО ДОПРОСНОГО
else:
    sleep(2)
    keyDown('s')
    sleep(0.5)
    keyUp('s')

    keyDown('d')
    sleep(0.5)
    keyUp('d')

    keyDown('s')
    sleep(0.5)
    keyUp('s')
    
    #ВОССТАНОВЛЕНИЕ МАНЫ
    #else:
        #sleep(2)
        #pydirectinput.PAUSE = 1
        #press('l')
        #press('l')
        #pydirectinput.PAUSE = 1.5
        #press('esc')
        #pydirectinput.PAUSE = 1
        #press('i')
        #moveTo(570, 390)
        #press('k')
        #moveTo(617, 306, 1)
        #press('k')
        #press('k')
        #press('k')
        #press('k')
        #press('k')
        #press('k')
        #press('l')
        #press('l')
        #press('k')
        #press('k')
        #moveTo(442, 470)
        #press('k')
        #moveTo(430, 540)
        #y+=1