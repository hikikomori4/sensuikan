#!/usr/bin/python3
# coding: utf-8

# Author: https://github.com/hikikomori4/sensuikan
# May the Force be with you!
# PyCharm must Die! 
# Использую быструю и легковесную среду разработки:
# http://geany.org/

import os
import sys
import shutil

# from resources import sea, uboat, locations

from resources import uboat, sea, locations, physics, encounters



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
    print_c('\nНачало\n')
    locations.loc_bridge()

def game_back():
    pass

def game_load():
    pass

def game_save():
    pass

def instruction():
    print('Описание игры....')
    print('''
    
    Картинка продольного разреза подводной лодки лодки "Средняя", серия IX-бис.'
    http://www.deepstorm.ru/DeepStorm.files/17-45/c%20IX/9-1.jpg
    
    ''')
    

    
   
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
 1) Начать новую игру   2) Инструкции   q) Выйти из игры
''')
    

     

   
actions = {
    '1': game_begin,
    'r': game_back,
    'l': game_load,
    's': game_save,
    '2': instruction,
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
