#!/usr/bin/python3
# coding: utf-8

from resources import uboat, sea

if __name__ == '__main__':
    print('Модуль отдельно не запускается!')



import os
def cls():
    try:
        os.system('clear')
    except:
        os.system('cls')


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
    print(__name__)


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
        'c1': rpt_C1,
        'c2': rpt_C2,
        'c3': rpt_C3,
        'c4': rpt_C4,
        'c5': rpt_C5,
        'c6': rpt_C6,
        'c7': rpt_C7,
        'с9': rpt_с9,
        'c0': rpt_C0,
        'r1': rpt_R1,
        'r2': rpt_R2,
        'r3': rpt_R3,
        'r4': rpt_R4,
        'r5': rpt_R5,
        'r7': rpt_R7,
        'r8': rpt_R8,
        '0': rpt_0
    }
    queryaction2(m_actions, m_text)
    # почему зацикливается на рапорте, не возвращаясь в отсек откуда вызвали?
     
      
      
     
#C1 - Первый отсек-убежище,торпедный
def rpt_C1():
    print('...')
    pass

#C2 - Второй отсек: аккумуляторный, каюта командира
def rpt_C2():
    pass

#C3 - Третий отсек-убежище: центральный пост
def rpt_C3():
    pass

#C4 - Четвёртый отсек: аккумуляторный
def rpt_C4():
    pass

#C5 - Пятый отсек: дизельный
def rpt_C5():
    pass

#C6 - Шестой отсек: электромоторный
def rpt_C6():
    pass

#C7 - Седьмой отсек-убежище: торпедный
def rpt_C7():
    pass

#с9 - Ходовой мостик
def rpt_с9():
    pass

#C0 - Боевая рубка
def rpt_C0(): 
    pass 

#R1 - балластным и топливным цистернам
def rpt_R1():
    
    print('Рапорт по балластным и топливным цистернам:\n')
    for ii in ('different1', 'different2', 'equalizing', 'quickdive', 'mainballast', 'torpedorshaped1', 'torpedorshaped2', 'fuel_tank1', 'fuel_tank2'):
        print(uboat.tanks[ii]['name'] + '. Состояние: ' + uboat.tanks[ii]['state'] + c_drk + \
        '\nобъём: ' + str(uboat.tanks[ii]['Capacity']['max']) + \
        ', принято забортной воды: ' + str(uboat.tanks[ii]['Capacity']['curr']) + ' тонн.\n' + c_nrm) 
         
        
    

        

#R2 - баллонам воздуха высокого давления
def rpt_R2():
    print('Рапорт по баллонам воздуха высокого давления:\n')
    for ii in range(14):
        if uboat.baloon_vvd[ii].condition == 0:
            b_cond = 'исправен'
        print('Объём баллона ' + str(ii) + ': ' + str(uboat.baloon_vvd[ii].capacity) + ', запас воздуха: ' + \
        str(uboat.baloon_vvd[ii].taken) + ', состояние: ' + b_cond)
    print()

#R3 - дизелям
def rpt_R3():
    pass

#R4 - электромоторам
def rpt_R4():
    pass

#R5 - аккумуляторным батареям
def rpt_R5():
    pass

#R7 - палубному орудию и снарядам
def rpt_R7():
    pass

#R8 - торпедным аппаратам и торпедам
def rpt_R8():
    pass
    
# Отмена рапорта
def rpt_0():
    pass
    
    
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
    
    

def queryaction(m_actions, m_text, m_locat):
    while True:
        
        printloc(m_locat[0], m_locat[1])
        
        print(m_text, end='')
        cmd = input(' ')
        menuact = m_actions.get(cmd)
    
        if menuact:
            menuact()
            
        else:
            print('\nНеизвестная команда.\n')
            queryaction(m_actions, m_text, m_locat)


def queryaction2(m_actions, m_text):

    print(m_text, end='')
    cmd = input(' ')
    menuact = m_actions.get(cmd)

    if menuact:
        menuact()
        
    else:
        print('\nНеизвестная команда.\n')



#########################################################



def loc_bridge():
    m_locat = (uboat.bridge[0]['name'], uboat.bridge[0]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Спуститься в рубку, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_0,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_0():

    m_locat = (uboat.compartments[0]['name'], uboat.compartments[0]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Спуститься в 3й отсек, '+c_inv+'2'+c_nrm+'-Подняться на мостик, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_3,
        '2': loc_bridge,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)
    
def loc_1():

    m_locat = (uboat.compartments[1]['name'], uboat.compartments[1]['desc'])
    m_text = c_inv+'2'+c_nrm+'-Перейти во 2й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '2': loc_2,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_2():

    m_locat = (uboat.compartments[2]['name'], uboat.compartments[2]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 1й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 3й отсек, '+c_inv+'C'+c_nrm+'-В каюту командира, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_1,
        '2': loc_3,
        'c': loc_2c,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_2c():

    m_locat = (uboat.cpt_cabin[0]['name'], uboat.cpt_cabin[0]['desc'])
    m_text = c_inv+'2'+c_nrm+'-Выйти из каюты, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '2': loc_2,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_3():

    m_locat = (uboat.compartments[3]['name'], uboat.compartments[3]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти во 2й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 4й отсек, '+c_inv+'3'+c_nrm+'-Подняться в боевую рубку, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_2,
        '2': loc_4,
        '3': loc_0,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_4():

    m_locat = (uboat.compartments[4]['name'], uboat.compartments[4]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 3й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 5й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_3,
        '2': loc_5,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_5():

    m_locat = (uboat.compartments[5]['name'], uboat.compartments[5]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 4й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 6й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_4,
        '2': loc_6,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_6():

    m_locat = (uboat.compartments[6]['name'], uboat.compartments[6]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 5й отсек, '+c_inv+'2'+c_nrm+'-Перейти в 7й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_5,
        '2': loc_7,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

def loc_7():

    m_locat = (uboat.compartments[7]['name'], uboat.compartments[7]['desc'])
    m_text = c_inv+'1'+c_nrm+'-Перейти в 6й отсек, '+c_inv+'S'+c_nrm+'-Отдать команду, '+c_inv+'R'+c_nrm+'-Запросить рапорт, '+c_inv+'L'+c_nrm+'-Осмотреться'
    m_actions = {
        '1': loc_6,
        's': commands,
        'r': reports,
        'l': look
        }
    queryaction(m_actions, m_text, m_locat)

