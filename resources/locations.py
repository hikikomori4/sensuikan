#!/usr/bin/python3
# coding: utf-8

from resources import uboat, sea

if __name__ == '__main__':
    print('Модуль отдельно не запускается!')



c_inv  = '\x1b\x5b\x37\x6d'
c_bld = '\x1b\x5b\x31\x6d'
c_drk = '\x1b\x5b\x32\x6d'
c_und = '\x1b\x5b\x34\x6d'
c_nrm = '\x1b\x5b\x30\x6d'


#####################
#  Игровые локации  #
#####################

def dummy():
    print('Пусто пока...')

def commands():
    print('Пусто пока...')


def reports():
     
    m_text ='''
         Запросить рапорт по отсекам:
         
    C1 - Первый отсек-убежище,торпедный
    C2 - Второй отсек: аккумуляторный, каюта командира
    C3 - Третий отсек-убежище: центральный пост
    C4 - Четвёртый отсек: аккумуляторный
    C5 - Пятый отсек: дизельный
    C6 - Шестой отсек: электромоторный
    C7 - Седьмой отсек-убежище: торпедный
    с9 - Ходовой мостик
    C0 - Боевая рубка
    
         Запросить рапорт по системам:
    
    R1 - балластным и топливным цистернам
    R2 - баллонам воздуха высокого давления
    R3 - дизелям
    R4 - электромоторам
    R5 - аккумуляторным батареям
    
         Запросить рапорт по вооружению:
    R7 - палубному орудию и снарядам
    R8 - торпедным аппаратам и торпедам
    
     0 - Отмена.'''
        
    m_actions = {
        'C1': dummy,
        'C2': dummy,
        'C3': dummy,
        'C4': dummy,
        'C5': dummy,
        'C6': dummy,
        'C7': dummy,
        'с9': dummy,
        'C0': dummy,
        'R1': dummy,
        'R2': dummy,
        'R3': dummy,
        'R4': dummy,
        'R5': dummy,
        'R7': dummy,
        'R8': dummy,
        '0': dummy
        }
    queryaction(m_actions, m_text)
    # почему зацикливается на рапорте, не возвращаясь в отсек откуда вызвали?
    
    
def look():
    globals() # Получение глобальных переменных 
    print('\n'+curr_desc2+'\n') 
    print('\nВаши текущие координаты: x = {}, y = {}, глубина = {}. \n' \
    .format(uboat.c_coord[0], uboat.c_coord[1],uboat.c_coord[2]))
      


def printloc(curr_loc, curr_desc):
    print(
    '\n       '+c_drk+'* * *'+c_nrm+'\n\n' +
    'Вы находитесь ' + c_und + curr_loc + c_nrm + '.\n')
    global curr_desc2  # объявление глобальной переменной 
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
    m_text = c_inv+'1'+c_nrm+'-Спуститься в рубку, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_0,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_0():

    printloc(uboat.compartments[0]['name'], uboat.compartments[0]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Спуститься в 3й отсек, '+c_inv+'2'+c_nrm+'-Подняться на мостик, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_3,
        '2': loc_bridge,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)
    
def loc_1():

    printloc(uboat.compartments[1]['name'], uboat.compartments[1]['desc'])
    m_text = c_inv+'2'+c_nrm+'-Перейти во 2й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '2': loc_2,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_2():

    printloc(uboat.compartments[2]['name'], uboat.compartments[2]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 1й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 3й отсек, '+c_inv+'C'+c_nrm+'-В каюту командира, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_1,
        '2': loc_3,
        'c': loc_2c,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_2c():

    printloc(uboat.cpt_cabin[0]['name'], uboat.cpt_cabin[0]['desc'])
    m_text = c_inv+'2'+c_nrm+'-Выйти из каюты, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '2': loc_2,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_3():

    printloc(uboat.compartments[3]['name'], uboat.compartments[3]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти во 2й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 4й отсек, '+c_inv+'3'+c_nrm+'-Подняться в боевую рубку, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_2,
        '2': loc_4,
        '3': loc_0,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_4():

    printloc(uboat.compartments[4]['name'], uboat.compartments[4]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 3й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 5й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_3,
        '2': loc_5,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_5():

    printloc(uboat.compartments[5]['name'], uboat.compartments[5]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 4й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 6й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_4,
        '2': loc_6,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_6():

    printloc(uboat.compartments[6]['name'], uboat.compartments[6]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 5й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 7й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_5,
        '2': loc_7,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

def loc_7():

    printloc(uboat.compartments[7]['name'], uboat.compartments[7]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 6й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_6,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text)

