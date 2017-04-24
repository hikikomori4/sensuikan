from resources import sea

from resources import uboat, sea, physics

# Только доклады о событиях.
# Сам ничего не меняет.
#


def onboard(*args):
    
    
    # Сообщает об работающих двигателях
        
    if uboat.engines['electro1']['rpm'] != 0 or uboat.engines['electro2']['rpm'] != 0:
        print('Работают электродвигатели...', end=' ')
    elif uboat.engines['diesel1']['rpm'] != 0 or uboat.engines['diesel2']['rpm'] != 0:
        print('Работают дизеля...', end=' ')
    elif uboat.engines['diesel1']['rpm'] == 0 or uboat.engines['diesel2']['rpm'] == 0:
        print('Все двигатели заглушены...', end=' ')
        
    # Сообщает о глубине погружения- всплытия   
        
    if uboat.c_coord[2] == 1:
        print ('ПЛ на поверхности в крейсерском положении.')
    elif uboat.c_coord[2] == 0:
        print ('ПЛ на поверхности в позиционном положении.')
    elif uboat.c_coord[2] < 0 and uboat.c_coord[2] >= uboat.PSCOPE_DEEP:
        print ('ПЛ на перископной глубине ' + str(uboat.c_coord[2]), end='')
    elif uboat.c_coord[2] < uboat.PSCOPE_DEEP and uboat.c_coord[2] >= uboat.SAFE_DEEP:
        print ('ПЛ на безопасной глубине ' + str(uboat.c_coord[2]), end='')
    elif uboat.c_coord[2] < uboat.SAFE_DEEP and uboat.c_coord[2] >= uboat.WORK_DEEP:
        print ('ПЛ на рабочей глубине ' + str(uboat.c_coord[2]), end='')
    elif uboat.c_coord[2] < uboat.WORK_DEEP and uboat.c_coord[2] >= uboat.MAX_DEEP:
        print ('ПЛ на предельной глубине ' + str(uboat.c_coord[2]), end='')
    elif uboat.c_coord[2] < uboat.MAX_DEEP and uboat.c_coord[2] >= uboat.CALC_DEEP:
        print ('ПЛ на предельной расчётной глубине ' + str(uboat.c_coord[2]), end='')
    elif uboat.c_coord[2] < uboat.CALC_DEEP:
        print ('ПЛ на запредельной глубине ' + str(uboat.c_coord[2]) + ',\nКорпус начинает деформироваться!!!' \
        + '\nДавление воды: ' + str(uboat.underwaterpressure))

    else:
        print ('Глубина - '+ str(uboat.c_coord[2]) + '. Непонятно, что случилось с глубиномером?!')
        
    print('\nДавление воды: ' + str(uboat.underwaterpressure) + ', плотность: ' + str(uboat.seadensity))
    
     
    
            
