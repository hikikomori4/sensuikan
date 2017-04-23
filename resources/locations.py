#!/usr/bin/python3
# coding: utf-8

from resources import uboat, sea, physics, encounters

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
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n')

    m_text ='''КОМАНДЫ:
    
        Перекладка положения рулей:
    1 - вертикального руля
    2 - носовых рулей глубины
    3 - кормовых рулей глубины
    
        Старт и останов двигателей:
    4 - Дизельных (только на поверхности или под РДП)
    5 - Электрических
    
        Продувка и приём забортной воды:
    a - Носовая дифферентная цистерна.
    b - Кормовая дифферентная цистерна.
    c - Уравнительная цистерна.
    d - Цистерна быстрого погружения.
    e - Цистерна главного балласта (ЦГБ)
    z - Срочное погружение! Заполнить цистерны: НД, КД, БП, ГБ! 
    x - Аварийное всплытие! Продуть ВСЕ цистерны!
    
    0 - Отмена

    '''




    m_actions = {
         '1': cmd_1,
         '2': cmd_2,
         '3': cmd_3,
         '4': cmd_4,
         '5': cmd_5,
         'a': cmd_a,
         'b': cmd_b,
         'c': cmd_c,
         'd': cmd_d,
         'e': cmd_e,
         'z': cmd_z,
         'x': cmd_x,
         '0': cmd_0
    }
    queryaction2(m_actions, m_text)


def cmd_1(): 
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n')  
    print('Текущее положение вертикального курсового руля: ' + str(uboat.v_rule))
    print('''
    Выберите значения: 0 - прямой руль, 
    положительное число - руль вправо на n град.
    отрицательное число - руль влево на n град.
    ''')
    nn = input('Введите новое значение (Enter - отмена): ')
    if not nn:
        nn = uboat.v_rule
    else:
        uboat.v_rule = int(nn)
        print('Задано новое значение: ' + str(uboat.v_rule))
     
def cmd_2(): 
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n')  
    print('Текущее положение носовых рулей глубины: ' + str(uboat.h_rule1))
    print('''
    Выберите значения: 0 - прямой руль, 
    положительное число - руль на всплытие на n град.
    отрицательное число - руль на погружение на n град.
    ''')
    nn = input('Введите новое значение (Enter - отмена): ')
    if not nn:
        nn = uboat.h_rule1
    else:
        uboat.h_rule1 = int(nn)
        print('Задано новое значение: ' + str(uboat.h_rule1))
    
         
def cmd_3(): 
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n')  
    print('Текущее положение кормовых рулей глубины: ' + str(uboat.h_rule2))
    print('''
    Выберите значения: 0 - прямой руль, 
    положительное число - руль на всплытие на n град.
    отрицательное число - руль на погружение на n град.
    ''')
    nn = input('Введите новое значение (Enter - отмена): ')
    if not nn:
        nn = uboat.h_rule2
    else:
        uboat.h_rule2 = int(nn)
        print('Задано новое значение: ' + str(uboat.h_rule2))
    
         
def cmd_4(): 
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n') 
    print('ДИЗЕЛЯ:\n')
    print('Текущее состояние двигателей: ' + str(uboat.engines['diesel1']['rpm']))
        
    if uboat.c_coord[2] < 0:
        print('Глубина ' + str(uboat.c_coord[2]) +' метров! Под водой запуск дизелей возможен только на перископной глубине под РДП.')
    else:
        print('''
    Выберите значения: 0 - СТОП машина, 
    положительное число - движение вперёд на оборотах от 100 до 7500.
    отрицательное число - аналогичное движение назад.
    ''')
        nn = input('Введите новое значение (Enter - отмена): ')
        if not nn:
            nn = uboat.engines['diesel1']['rpm']
        elif (int(nn) > -7501 and int(nn) < -99) or (int(nn) > 99 and int(nn) < 7501) or int(nn) == 0:
            uboat.engines['diesel1']['rpm'] = int(nn)
            print('Задано новое значение: ' + str(uboat.engines['diesel1']['rpm']))
            uboat.engines['diesel2']['rpm'] = uboat.engines['diesel1']['rpm']
        else:
            print(c_und +'Ошибка. Значение должно быть в диапазоне 100-7500 оборотов!' + c_nrm)
        
           
def cmd_5(): 
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n') 
    print('ЭЛЕКТРОДВИГАТЕЛИ:\n')
    print('Текущее состояние двигателей: ' + str(uboat.engines['electro1']['rpm']))
    print('''    
    Выберите значения: 0 - СТОП машина, 
    положительное число - движение вперёд на оборотах от 100 до 3500.
    отрицательное число - аналогичное движение назад.
    ''')
    nn = input('Введите новое значение (Enter - отмена): ')
    if not nn:
        nn = uboat.engines['electro1']['rpm']
    elif (int(nn) > -3501 and int(nn) < -99) or (int(nn) > 99 and int(nn) < 3501) or int(nn) == 0:
        uboat.engines['electro1']['rpm'] = int(nn)
        print('Задано новое значение: ' + str(uboat.engines['electro1']['rpm']))
        uboat.engines['electro2']['rpm'] = uboat.engines['electro1']['rpm']
    else:
        print(c_und +'Ошибка. Значение должно быть в диапазоне 100-3500 оборотов!' + c_nrm)
        
        
           
    
#######################################################################
# Заполнение и продувка балластных цистерн
#######################################################################

def tanks_operate(tankname, tankmax, tankcurr ):    
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n') 
    print(tankname + '\n')
    
    print('Воздуха в каждом из баллонов ВВД: \n')
    for i in range(14):
        print(uboat.baloon_vvd[i].taken, end= ',')
    
    vvd_all = 0
    for i in range(14):
        vvd_all += int(uboat.baloon_vvd[i].taken)

    print('\nВсего запасов ВВД: ' + str(vvd_all),'\n')
    
    if tankcurr == 0:
        print('Цистерна пуста. Можно принять до ' + str(tankmax) + ' тонн.')
    elif tankcurr == tankmax:
        print('Цистерна полна! Можно откачать до ' + str(tankmax) + ' тонн.')
    else:
        print('В цистерну принято '+ str(tankcurr) +' тонн забортной воды из ' + str(tankmax) + ' возможных.')
    
    i = int(input('\n' +
    ' 1 - Принять воду в цистерну\n' +
    ' 2 - Откачать воду воздухом высокого давления\n' + 
    ' 0 - Отмена\n\n '))
    # -------------------------------------------------------------     
    if i == 1:
        n = int(input('\nСколько тонн воды принять? '))

        if n < int((tankmax - tankcurr + 1)):
            tankcurr += n
            print('В цистерну принято ' + str(n) + ' тонн. Сейчас в ней ' + str(tankcurr) + ' тонн заботной воды.')
            global tmp
            tmp = tankcurr
            
        else:
            print('Нельзя принять больше объёма цистерны!')
        

    # -------------------------------------------------------------     
    elif i == 2:
        n = int(input('Сколько тонн воды откачать? ')) # Проверка не превышает ли запрос имеющуюся воду
        if n < int(tankcurr + 1):
            for i in range(14):
                                                    # Если в баллоне больше, чем запрашиваемый объём
                if uboat.baloon_vvd[i].taken > n:   
                    uboat.baloon_vvd[i].taken -= n  # Расход ВВД
                    break
                    
                else:
                    continue
            tankcurr -= n                      # вытеснение воды из танка
            global tmp
            tmp = tankcurr
            print('Из цистерны продуто ' + str(n) + ' тонн. Сейчас в ней осталось ' + str(tankcurr) + ' тонн заботной воды.')


        else:
            print('Нельзя откачать воды больше, чем есть в цистерне!')
    # -------------------------------------------------------------     
        
    elif i == 0:
        print('Отмена действия.')
    
    return tmp
    
    
#######################################################################

def cmd_a():
    tanks_operate(
        uboat.tanks['different1']['name'],
        uboat.tanks['different1']['Capacity']['max'],
        uboat.tanks['different1']['Capacity']['curr'] )
    uboat.tanks['different1']['Capacity']['curr'] = tmp

def cmd_b(): 
    tanks_operate(
        uboat.tanks['different2']['name'],
        uboat.tanks['different2']['Capacity']['max'],
        uboat.tanks['different2']['Capacity']['curr'] )
    uboat.tanks['different2']['Capacity']['curr'] = tmp

          
def cmd_c(): 
    tanks_operate(
        uboat.tanks['equalizing']['name'],
        uboat.tanks['equalizing']['Capacity']['max'],
        uboat.tanks['equalizing']['Capacity']['curr'] )
    uboat.tanks['equalizing']['Capacity']['curr'] = tmp

    
         
def cmd_d():
    tanks_operate(
        uboat.tanks['quickdive']['name'],
        uboat.tanks['quickdive']['Capacity']['max'],
        uboat.tanks['quickdive']['Capacity']['curr'] )
    uboat.tanks['quickdive']['Capacity']['curr'] = tmp   

    
          
def cmd_e(): 
    tanks_operate(
        uboat.tanks['mainballast']['name'],
        uboat.tanks['mainballast']['Capacity']['max'],
        uboat.tanks['mainballast']['Capacity']['curr'] )
    uboat.tanks['mainballast']['Capacity']['curr'] = tmp



def cmd_z(): 
    
    print(c_bld + c_und +'\nВнимание! Боевая тревога! Срочное погружение!\n' + c_nrm)
    print('Полностью заполняются балластные цистерны:\n\n  ' + uboat.tanks['mainballast']['name'])
    print('  ' + uboat.tanks['different1']['name'])
    print('  ' + uboat.tanks['different2']['name'])
    print('  ' + uboat.tanks['equalizing']['name'])
    print('\nКроме:\n\n  ' + uboat.tanks['quickdive']['name'] + '\n')
    
   
    
    uboat.tanks['mainballast']['Capacity']['curr'] = uboat.tanks['mainballast']['Capacity']['max'] 
    uboat.tanks['different1']['Capacity']['curr'] = uboat.tanks['different1']['Capacity']['max'] 
    uboat.tanks['different2']['Capacity']['curr'] = uboat.tanks['different2']['Capacity']['max'] 
    uboat.tanks['equalizing']['Capacity']['curr'] = uboat.tanks['equalizing']['Capacity']['max'] 


def cmd_x(): 

    print(c_bld + c_und +'\nВнимание! Боевая тревога! Аварийное всплытие!\n' + c_nrm)
    print('Будут продуты все цистерны без исключения!\n\n')

    tnks =    ( uboat.tanks['mainballast']['Capacity']['curr'],
                uboat.tanks['different1']['Capacity']['curr'],
                uboat.tanks['different2']['Capacity']['curr'],
                uboat.tanks['equalizing']['Capacity']['curr'],
                uboat.tanks['quickdive']['Capacity']['curr']  )

    for o in  tnks:

        for i in range(14):
                                                # Если в баллоне больше, чем запрашиваемый объём
            print('.', end='')
            if uboat.baloon_vvd[i].taken > o:
                uboat.baloon_vvd[i].taken -= o  # Расход ВВД
                tnks = 0
                break
                
            else:
                continue
    
    print('\nОстаток воздуха в каждом из баллонов ВВД: \n')
    for i in range(14):
        print(uboat.baloon_vvd[i].taken, end= ' ')
    print('\n')


    #if uboat.subsea > sum(tnks):
        #print('Плохие новости... У нас нехватает запасов ВВД,\n' + \
            #'чтобы всплыть. Но... возможно ещё не все потеряно, если\n' + \
            #'попробовать продуть ЦГБ остатками вручную, и всплыть на рулях.\n')
    
          
def cmd_0(): 
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n')  
         


def reports():
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n')
    m_text ='''РАПОРТЫ:
    
     1 - Снять показания с приборов навигации
         и положения ДПЛ в пространстве
        
     2 - Запросить рапорт по всем отсекам.
    
         Запросить рапорт по системам:
    
     3 - балластным и топливным цистернам
     4 - баллонам воздуха высокого давления
     5 - электромоторам и дизелям
     6 - аккумуляторным батареям
    
         Запросить рапорт по вооружению:

     7 - палубному орудию и снарядам
     8 - торпедным аппаратам и торпедам
    
     0 - Отмена.'''
        
    m_actions = {
         '1': rpt_r,
         '2': rpt_c,
         '3': rpt_R1,
         '4': rpt_R2,
         '5': rpt_rd,
         '6': rpt_ra,
         '7': rpt_R7,
         '8': rpt_R8,
         '0': rpt_0
    }
    queryaction2(m_actions, m_text)
    
     
     
      
def rpt_r():
    print('\n       '+c_drk+'* * *'+c_nrm+'\n\n' + \
    '\nВаши текущие координаты на карте: x = {}, y = {}, глубина = {}.\nСкорость: {} узлов.' \
    .format(uboat.c_coord[0], uboat.c_coord[1],uboat.c_coord[2], uboat.speed))

    if uboat.c_differ == 0:
        c_differ_t = 'отсутствует'
    elif uboat.c_differ > 0:
        c_differ_t = 'на нос ' + str(uboat.c_differ) + ' градус(а)'
    elif uboat.c_differ < 0:
        c_differ_t = 'на корму ' + str(uboat.c_differ) + ' градус(а)'

    if uboat.c_kren == 0:
        c_kren = 'отсутствует'
    elif uboat.c_kren > 0:
        c_kren = 'на правый борт ' + str(uboat.c_kren) + ' градус(а)'
    elif uboat.c_kren < 0:
        c_kren = 'на левый борт ' + str(uboat.c_kren) + ' градус(а)'
    
    print('\nДифферент ' + c_differ_t + '. ' + 'Крен ' + c_kren + '.\n' )
    
    if uboat.v_rule == 0:
        v_rule = 'прямо по курсу'
    elif uboat.v_rule > 0:
        v_rule = 'на правый борт ' + str(uboat.v_rule) + ' градус(а)'
    elif uboat.v_rule < 0:
        v_rule = 'на левый борт ' + str(uboat.v_rule) + ' градус(а)'

    if uboat.h_rule1 == 0:
        h_rule1 = 'горизонтальное'
    elif uboat.h_rule1 > 0:
        h_rule1 = 'на всплытие ' + str(uboat.h_rule1) + ' градус(а)'
    elif uboat.h_rule1 < 0:
        h_rule1 = 'на погружение ' + str(uboat.h_rule1) + ' градус(а)'
      
    if uboat.h_rule2 == 0:
        h_rule2 = 'горизонтальное'
    elif uboat.h_rule2 > 0:
        h_rule2 = 'на всплытие ' + str(uboat.h_rule2) + ' градус(а)'
    elif uboat.h_rule2 < 0:
        h_rule2 = 'на погружение ' + str(uboat.h_rule2) + ' градус(а)'

    print('          | вертикального руля - ' + v_rule + '.')
    print('Положение | носовых рулей глубины - ' + h_rule1 + \
    '. \n          | кормовых рулей глубины - ' + h_rule2 + '.')

    
     
#C1 - Первый отсек-убежище,торпедный
def rpt_c():
     
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n\nДоклад о состоянии отсеков ДПЛ:\n\n' +
    
    'В ' + uboat.bridge[0]['name'] + ' ' + c_drk + uboat.bridge[0]['state'] + c_nrm + 
    '\nВ ' + uboat.cpt_cabin[0]['name'] + ' ' + c_drk + uboat.cpt_cabin[0]['state'] + c_nrm )
    
    for ii in range(1,8):
        print('В ' + uboat.compartments[ii]['name'] + ' ' + c_drk + uboat.compartments[ii]['state'] + c_nrm)


#R1 - балластным и топливным цистернам
def rpt_R1():
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n')
    print('Рапорт по балластным и топливным цистернам:\n')
    for ii in ('different1', 'different2', 'equalizing', 'quickdive', 
                'mainballast', 'torpedorshaped1', 'torpedorshaped2', 
                'fuel_tank1', 'fuel_tank2'):
        print(uboat.tanks[ii]['name'].ljust(32) +' ' + c_drk +  \
        uboat.tanks[ii]['state'] + ', объём: ' + str(uboat.tanks[ii]['Capacity']['max']) + \
        ', принято: ' + str(uboat.tanks[ii]['Capacity']['curr']) + ' тонн.' + c_nrm) 
         
        
    
        

#R2 - баллонам воздуха высокого давления
def rpt_R2():
    print('Рапорт по баллонам воздуха высокого давления:\n')
    for ii in range(14):
        if uboat.baloon_vvd[ii].condition == 0:
            b_cond = 'исправен'
        print('Объём баллона ' + str(ii) + ': ' + str(uboat.baloon_vvd[ii].capacity) + ', запас воздуха: ' + \
        str(uboat.baloon_vvd[ii].taken) + ', состояние: ' + b_cond)
    print()

 
def rpt_rd():
 
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n\nДоклад по двигателям:\n')

    print('Дизель 1 ' + uboat.engines['diesel1']['state'] + ', обороты - ' + str(uboat.engines['diesel1']['rpm'])+ ".") 
    print('Дизель 2 ' + uboat.engines['diesel2']['state'] + ', обороты - ' + str(uboat.engines['diesel2']['rpm'])+ ".")
    print('Электродвигатель 1 ' + uboat.engines['electro1']['state'] + ', обороты - ' + str(uboat.engines['electro1']['rpm'])+ ".")
    print('Электродвигатель 2 ' + uboat.engines['electro2']['state'] + ', обороты - ' + str(uboat.engines['electro2']['rpm'])+ ".")


#R5 - аккумуляторным батареям
def rpt_ra():
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n\nДоклад по АКБ:\n')
    print('\nПриблизительный запас хода: ' + str(uboat.battery_cell_h) +'\n')
    print('Напряжения на 62-х элементах 1й группы АКБ:', uboat.battery1)
    print()
    print('Напряжения на 62-х элементах 2й группы АКБ:', uboat.battery1)
    
    

#R7 - палубному орудию и снарядам
def rpt_R7():
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n\nЭто учебное судно, вооружение демонтировано до окончания ходовых испытаний.\n')

#R8 - торпедным аппаратам и торпедам
def rpt_R8():
    print('\n            ' + c_drk + '* * *' + c_nrm + '\n\nЭто учебное судно, вооружение демонтировано до окончания ходовых испытаний.\n')
    
# Отмена рапорта
def rpt_0():
    pass
    
    
def look():
    globals() # Получение глобальных переменных 
    print('\n'+curr_desc2+'\n') 
 
def printloc(curr_loc, curr_desc):
    
    if curr_loc == uboat.bridge[0]['name']:
        vna = 'на '
    else:
        vna = 'в '
        
    print(
    '\n       '+c_drk+'* * *'+c_nrm+'\n\n' +
    'Вы находитесь ' + vna + c_und + curr_loc + c_nrm + '.\n')
    global curr_desc2  # объявление глобальной переменной 
    curr_desc2 = curr_desc
    
    

def queryaction(m_actions, m_text, m_locat):

    while True:
        
        printloc(m_locat[0], m_locat[1])
        
        #  =====================================
        #  Каждый цикл отображения меню вызывает
        #  обработчики игровой физики и событий
        #  =====================================
        
        physics.uboatf()      
        encounters.onboard()  
        
        
        print('\n', m_text, end='')
        cmd = input(' ')
        menuact = m_actions.get(cmd)
    
        if menuact:
            menuact()
            
        else:
            print('\nНеизвестная команда.')
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

