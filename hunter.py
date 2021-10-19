import time
import timeit

import pydirectinput
from time import sleep, time
from pydirectinput import moveTo
from pydirectinput import press
from pydirectinput import click
from pydirectinput import keyDown
from pydirectinput import keyUp
from pydirectinput import mouseDown
from pydirectinput import mouseUp
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_loop
from python_imagesearch.imagesearch import imagesearch_region_loop


import cProfile


def press_print(sec, btn, name, start_time):
    press(btn)
    print(str(round(time() - start_time, 2)) + ' - ' + str(sec) + ' - ' + str(btn) + ' - ' + name)
    sleep(sec)

def sleep_time_dif(sec, start_time):
    print(round(time() - start_time, 2))


def pic_search_click(path_pic):
    adress = 'path_pics/'+str(path_pic)
    r = 0
    while r<4:
        pos = imagesearch(adress, 0.5)
        if pos[0] != -1:
            mouseDown(pos[0] + 50, pos[1] + 240)
            sleep(0.1)
            mouseUp()
        else:
            print('Image not found')
        sleep(1)
        r+=1

def moveWASD(direction, duration):
    sleep(0.5)
    for key in direction:
        keyDown(key)
    sleep(duration)
    for key in direction:
        keyUp(key)
    sleep(0.5)

def amIin(menu_name):
    adress = 'path_pics/'+str(menu_name )
    if imagesearch_loop(adress, 0.5)[0] >= 0:
        return True

def findAndClick(str):
    adress = 'path_pics/' + str
    pos =imagesearch_loop(adress, 0.5)
    if pos[0] >= 0:
        moveTo(pos[0] + 20, pos[1] + 20,1)
        mouseDown(pos[0] + 20, pos[1] + 20)
        mouseUp()

def gotoInterrogarion():
    # идем туда
    sleep(1)
    press('esc')
    sleep(1)
    moveWASD(['s', 'd'], 1.5)
    moveWASD(['s'], 1)
    moveWASD(['d'], 4)
    pic_search_click('interrogation.png')
    #press('k')

def gotoDimensionGuide():
    sleep(1)
    press('esc')
    sleep(1)

    pos = imagesearch('path_pics/find ladder.png', 0.8)
    mouseDown(pos[0]+100, pos[0]-50)
    sleep(0.01)
    mouseUp()
    sleep(0.1)

    moveWASD(['w', 'a'], 1.5)
    moveWASD(['a'], 2)
    moveWASD(['w'], 1.2)
    moveWASD(['w', 'a'], 1.3)
    pic_search_click('dimension_guide.png')
    # press('k')

def getMana():
    sleep(2)
    pydirectinput.PAUSE = 1
    press('l')
    press('l')
    pydirectinput.PAUSE = 1.5
    press('esc')
    pydirectinput.PAUSE = 1
    press('i')
    moveTo(570, 390)
    press('k')
    moveTo(617, 306, 1)
    press('k')
    press('k')
    press('k')
    press('k')
    press('k')
    press('k')
    press('l')
    press('l')
    press('k')
    press('k')
    moveTo(442, 470)
    press('k')
    moveTo(430, 540)

def killTwoFive():
    x = 1
    while x <= 1000:
        pydirectinput.PAUSE = 0.5
        moveTo(1400, 900)  # на тайл
        sleep(0.5)
        press_print('k', 'имя карты')  # имя карты
        pydirectinput.PAUSE = 1.2
        press_print('k', 'да в диалоге')  # да в диалоге
        pydirectinput.PAUSE = 0.4
        press_print('k', 'на дебаф')  # на дебаф
        press_print('k', 'на панель')  # на пaнель
        press_print('k', 'выбираем Киллиа')  # выбираем Киллиа
        press_print('k', 'выбираем MOVE')  # выбираем MOVE
        moveTo(600, 240)  # на тайл
        press_print('k', 'подтвердить движение')  # подтвердить движение
        press_print('4', 'special')  # special
        press_print('k', 'cap2 select')  # cap2 select
        press_print('k', 'cap2 confirm')  # cap2 confirm
        pydirectinput.PAUSE = 1.5
        press_print('2', 'end turn')  # end turn
        # press_print('esc','3 captured')#3 captured
        press_print('k', 'награды')  # награды
        pydirectinput.PAUSE = 0.1
        press_print('k', 'экспа')  # экспа
        x += 1
        press_print('k', 'просто')  # награды
        press_print('k', 'закрыть')  # награды
        pydirectinput.PAUSE = 1
        press_print('esc', 'так')  # награды

def captureTwoFive(y):
    sleep(1)
    x = 0
    while x < y:
        r = time()
        moveTo(1400, 900,1)  # на тайл
        sleep(1)
        findAndClick('hazardous_highway_4.png')  # имя карты
        sleep(.6)

        press_print(3.2, 'k', 'да в диалоге', r)  # да в диалоге
        press_print(1.3, 'k', 'на дебаф', r)  # на дебаф
        #экшон
        press_print(.5, 'k', 'на панель', r)  # на пaнель
        press_print(.5, 'k', 'выбираем Киллиа', r)  # выбираем Киллиа
        press_print(1, 'k', 'выбираем MOVE', r)  # выбираем MOVE

        moveTo(600, 240)  # на тайл
        sleep(.5)

        press_print(.5, 'k', 'подтвердить движение', r)  # подтвердить движение
        press_print(.5, '4', 'special', r)  # special
        press_print(.5, 'k', 'cap2 select', r)  # cap2 select
        press_print(.5, 'k', 'cap2 confirm', r)  # cap2 confirm
        press_print(2, '2', 'end turn', r)  # end turn
        press_print(2.5, 'k','3 captured', r)  # 3 captured
        press_print(.4, 'k', 'награды1', r)  # награды
        press_print(2, 'k', 'награды2', r)  # награды
        press_print(1, 'k', 'экспа', r)  # экспа
        press_print(.7, 'k', 'просто', r)  # награды
        press_print(.7, 'k', 'закрыть', r)  # награды
        #press_print(.7, 'k', 'деньги', r)  # награды

        x += 1
        sleep(0.3)

        print('Цикл :' + str(x) + ' из ' + str(y))
        sleep(0.3)

def interrogateAndExtract():
    sleep(1)
    press('l')
    sleep(1)
    press('l')
    sleep(1)
    press('l')
    sleep(1)
    # идем туда
    gotoInterrogarion()

    #Interrogation

    findAndClick('interrogate.png')
    sleep(1)

    #начали пытать
    if amIin('interrogation list.png'):
        interr = 0
        while interr <= 5:
            sleep(0.5)
            press('k')
            press('k')
            sleep(1)
            interr += 1
        #закончили пытать
        sleep(1)
        press('l')
        sleep(1)

    #Extract
    findAndClick('extract.png')
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
    sleep(2)

    # идем обратно
    gotoDimensionGuide()

def extractElixirs(c):
    #if amIin('netherworld.png'):
    findAndClick('poisondise.png')
    captureTwoFive(c)
    interrogateAndExtract()
    extractElixirs(c)

#общий слип перед началом каких-либо функций
sleep(1)

#pic_search_click('dimension_guide.png')
#pic_search_click('interrogation.png')
#gotoInterrogarion()
#gotoDimensionGuide()
#extractElixirs(42)

captureTwoFive(11)


