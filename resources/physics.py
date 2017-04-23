#!/usr/bin/python3
# coding: utf-8

from resources import uboat, sea




# Игровая физика
# Взаимодействие ДПЛ с объектами в зависимости от изменения параметров.


# Изменения дифферента
def uboatf(*args):
    
    
    #
    # Изменение дифферента:
    #
    global c_differ
    if uboat.tanks['different1']['Capacity']['curr'] > uboat.tanks['different2']['Capacity']['curr']:
        uboat.c_differ_max1 = int(uboat.tanks['different1']['Capacity']['curr'] - uboat.tanks['different2']['Capacity']['curr'])/ 100
        if uboat.c_differ < uboat.c_differ_max1:
            uboat.c_differ += uboat.c_differ_max1/10
            
    elif uboat.tanks['different2']['Capacity']['curr'] > uboat.tanks['different1']['Capacity']['curr']:
        uboat.c_differ_max2 = int(uboat.tanks['different2']['Capacity']['curr'] - uboat.tanks['different1']['Capacity']['curr'])/ 100
        if uboat.c_differ < uboat.c_differ_max2:
            uboat.c_differ += uboat.c_differ_max2/10
    

    #
    # Изменение плавучести\глубины в зависимости от приёма воды
    #
    global waterloaded
    
    # вычисление объёма принятой воды в данный отрезок времени:
    waterloaded = (
        uboat.tanks['different1']['Capacity']['curr'] + \
        uboat.tanks['different2']['Capacity']['curr'] + \
        uboat.tanks['mainballast']['Capacity']['curr'] + \
        uboat.tanks['equalizing']['Capacity']['curr'] + \
        uboat.tanks['quickdive']['Capacity']['curr'] )

    # задание ускорения погружения-всплытия ДПЛ

    # Если принято воды >= необходимой для погружения
    #   если Пл не глубже 150 метров
    #       увеличить глубину на 1 метр

    if waterloaded >= uboat.subsea:
        if uboat.c_coord[2] > -150:
            uboat.c_coord[2] = uboat.c_coord[2]-1

    # Если принято воды < необходимой для погружения
    #   Если глубина меньше 0
    #       уменьшить глубину на 1 метр

    elif waterloaded < uboat.subsea:
        if uboat.c_coord[2] <= 0:
            uboat.c_coord[2] = uboat.c_coord[2]+1



# ---------------------------------------------------------
# Глубокое синее море...
# Свалка говнокода крабам.

    #elif waterloaded >= uboat.subsea:
        #if uboat.c_coord[2] < -30:
            #uboat.c_coord[2] = uboat.c_coord[2]-1
 
    # Задание статичного положения ДПЛ
 
    #if waterloaded <= uboat.cruiser:
        #uboat.c_coord[2] = 1
    #elif waterloaded <= uboat.position:
        #uboat.c_coord[2] = 0
    

    #for n in ('different1', 'different2', 'equalizing', 'quickdive', 'mainballast'):
        # = uboat.tanks[n]['Capacity']['curr']
        #print(uboat.tanks[n]['Capacity']['curr'], flotation)
#def uboat(*args):
    #global c_differ
    #if uboat.tanks['different1']['Capacity']['curr'] != uboat.tanks['different2']['Capacity']['curr']:
        #c_differ = str(uboat.tanks['different1']['Capacity']['curr'] - uboat.tanks['different2']['Capacity']['curr'])
#    print(uboat.c_differ)
#    print((int(uboat.tanks['different1']['Capacity']['curr'] - uboat.tanks['different2']['Capacity']['curr'])/ 100 ))
