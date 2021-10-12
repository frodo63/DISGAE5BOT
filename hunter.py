import pydirectinput
from time import sleep
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

def press_print(btn, name):
    print('pressed ' + str(btn) + ' - ' + name)
    press(btn)

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


def findAndClick(menu_name):
    adress = 'path_pics/' + str(menu_name)
    pos =imagesearch_loop(adress, 0.5)
    if pos[0] >= 0:
        moveTo(pos[0] + 20, pos[1] + 20,1)
        click(pos[0] + 20, pos[1] + 20)
        mouseUp()

def gotoInterrogarion():
    pydirectinput.PAUSE = 0
    # идем туда
    sleep(1)
    press('esc')
    sleep(1)
    moveWASD(['s', 'd'], 1.5)
    moveWASD(['s'], 1)
    moveWASD(['d'], 4)
    pic_search_click('interrogation.png')

def gotoDimensionGuide():
    pydirectinput.PAUSE = 0
    sleep(1)
    press('esc')
    sleep(1)
    moveWASD(['s', 'a'], 0.15)
    moveWASD(['w', 'a'], 1.5)
    moveWASD(['a'], 2)
    moveWASD(['w'], 1.2)
    moveWASD(['w','a'], 1.5)
    pic_search_click('dimension_guide.png')

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

def captureTwoFive():
    moveTo(1400, 900)  # на тайл
    if amIin('poisondise_inside.png'):
        findAndClick('hazardous_highway_4.png')  # имя карты
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
    press_print('2', 'end turn')  # end turn
    pydirectinput.PAUSE = 1.5
    press_print('esc','3 captured')#3 captured
    pydirectinput.PAUSE = 0.1
    press_print('k', 'награды')  # награды
    press_print('k', 'ты уже')  # награды
    press_print('k', 'экспа')  # экспа
    press_print('k', 'просто')  # награды
    pydirectinput.PAUSE = 1
    press_print('esc', 'так')  # награды

def interrogateAndExtract():
    press('l')
    sleep(0.5)
    press('l')
    sleep(0.5)
    # идем туда
    gotoInterrogarion()

    #Interrogation
    if amIin('Interrogation Room.png'):
        findAndClick('interrogate.png')
    sleep(1)

    #начали пытать
    interr = 0
    while interr<=5:
        sleep(0.5)
        press('k')
        press('k')
        sleep(1)
        interr+=1
    #закончили пытать
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

def extractElixirs():
    if amIin('netherworld.png'):
        findAndClick('poisondise.png')
    sleep(1)
    x = 1
    while x < 3:
        captureTwoFive()
        print('\b Цикл : ' + str(x) + ' из 42. Пленных примерно: ' + str(x*3))
        x+=1
    else:
        interrogateAndExtract()
        extractElixirs()

#общий слип перед началом каких-либо функций
sleep(3)

#pic_search_click('dimension_guide.png')
#pic_search_click('interrogation.png')
#gotoInterrogarion()
#gotoDimensionGuide()
extractElixirs()
