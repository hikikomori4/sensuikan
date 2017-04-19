#!/usr/bin/python3
# coding: utf-8

# May the Force be with you

import os
import sys
import shutil
from resources import sea, uboat, locations



def cls():
    try:
        os.system('clear')
    except:
        os.system('cls')


def print_c(line):
    lines = [line]
    width = shutil.get_terminal_size().columns
    position = (width - max(map(len, lines))) // 2
    for line in lines: # left justtified
        print(' '* position + line)


def game_begin():
    cls()
    print_c('Начало')
    locations.loc_bridge()

def game_back():
    pass

def game_load():
    pass

def game_save():
    pass

def instruction():
    print('Описание игры....')
   
def game_exit():
    print('\nЗавершение программы...\n')
    sys.exit(0)



def show_mainmenu():
    cls()
    print('\n',
    ' ИГРА-СИМУЛЯТОР дизель-электрической подводной лодки.\n',
    ' СССР, период Великой Отечественной Войны 1941-1945.\n',
    ' ДПЛ тип "Средняя", серия IX-бис.',
r"""
 
                            /``:_
   ,----....____            |    `:.
  (             ````----....|___   |
   \     _                      ````----....____
    \   `_)                                     ```---.._
     \                                                   \
   )`.\  )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.  
 -'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-""")
    
    print('''
 b) Начать новую игру
 r) Вернуться в текущую
 l) Загрузить игру
 s) Сохранить игру
 i) Инструкции
 q) Выйти из игры
 
    ''')
    # print(uboat.compartments['mainballast']['Capacity']['max'])
    #print(uboat.compartments[2]['desc'])
    #print(uboat.compartments[4]['truim'])
    # print(uboat.battery1)
    #print(uboat.elmotor['rpm'])
    #print(uboat.compartments[1]['name'])
    

     

   
actions = {
    'b': game_begin,
    'r': game_back,
    'l': game_load,
    's': game_save,
    'i': instruction,
    'm': show_mainmenu,
    'q': game_exit
    }
   

if __name__== '__main__':
    show_mainmenu()

    while True:
        cmd = input('Ваша команда? > ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('\nНеизвестная команда. m) Вернуться к меню.\n')


# def show_mai1nmenu():
