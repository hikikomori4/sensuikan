#!/usr/bin/python3
# coding: utf-8

from resources import uboat

if __name__ == '__main__':
    print('Модуль отдельно не запускается!')


c_inv  = '\x1b\x5b\x37\x6d'
c_bld = '\x1b\x5b\x31\x6d'
c_drk = '\x1b\x5b\x32\x6d'
c_und = '\x1b\x5b\x34\x6d'
c_nrm = '\x1b\x5b\x30\x6d'



'''
Мостик
1-Спуститься в рубку, S-Отдать команду, L-Осмотреться


Боевая рубка
1-Спуститься в 3й отсек, 2-Подняться на мостик, S-Отдать команду, L-Осмотреться


Первый отсек-убежище
1-Перейти во 2й отсек, S-Отдать команду, L-Осмотреться

Второй отсек: аккумуляторный
1-Перейти в 3й отсек, 2-Перейти в 1й отсек, S-Отдать команду, L-Осмотреться, C-В каюту командира

Третий отсек-убежище
1-Перейти во 2й отсек, 2-Перейти в 4й отсек, 3-Подняться в боевую рубку, S-Отдать команду, L-Осмотреться


Четвёртый отсек: аккумуляторный
1-Перейти в 3й отсек, 2-Перейти в 5й отсек, S-Отдать команду, L-Осмотреться


Пятый отсек: дизельный
1-Перейти в 6й отсек, 2-Перейти в 4й отсек, S-Отдать команду, L-Осмотреться


Шестой отсек: электромоторный
1-Перейти в 5й отсек, 2-Перейти в 7й отсек, S-Отдать команду, L-Осмотреться


Седьмой отсек-убежище
1-Перейти в 6й отсек, S-Отдать команду, L-Осмотреться
'''


##########################################################


def dummy():
    pass



def commands():
    pass
    
def look():
    globals()
    print(curr_desc2)   # нужно сюда....


def printloc(curr_loc, curr_desc):
    print(
    '\n       '+c_drk+'* * *'+c_nrm+'\n\n' +
    'Вы находитесь ' + c_und + curr_loc + c_nrm + '.\n' +
    '\n' + curr_desc + '\n' )
    global curr_desc2
    curr_desc2 = curr_desc
    
    

def queryaction(m_actions, m_text):
    while True:
        print(m_text, end='')
        cmd = input(' ')
        menuact = m_actions.get(cmd)

        if menuact:
            menuact()
        else:
            print('\nНеизвестная команда.\n')

#########################################################



def loc_bridge():
    printloc(uboat.bridge[0]['name'], uboat.bridge[0]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Спуститься в рубку, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_0,
        's': commands,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_0():

    printloc(uboat.compartments[0]['name'], uboat.compartments[0]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Спуститься в 3й отсек, '+c_inv+'2'+c_nrm+'-Подняться на мостик, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_3,
        '2': loc_bridge,
        's': commands,
        'l': look
        }
    queryaction(m_actions, m_text)
    

def loc_3():

    printloc(uboat.compartments[3]['name'], uboat.compartments[3]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти во 2й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 4й отсек, '+c_inv+'3'+c_nrm+'-Подняться в боевую рубку, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': dummy,
        '2': dummy,
        '3': loc_0,
        's': commands,
        'l': look
        }
    queryaction(m_actions, m_text)










