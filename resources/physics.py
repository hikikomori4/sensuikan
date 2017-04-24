#!/usr/bin/python3
# coding: utf-8

from resources import uboat, sea


# Игровая физика
# Взаимодействие ДПЛ с объектами в зависимости от изменения параметров.


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
    global underwaterpressure
    global fixingfloat
    global seadensity
    
    # вычисление объёма принятой воды в данный отрезок времени:
    waterloaded = (
        uboat.tanks['different1']['Capacity']['curr'] + \
        uboat.tanks['different2']['Capacity']['curr'] + \
        uboat.tanks['mainballast']['Capacity']['curr'] + \
        uboat.tanks['equalizing']['Capacity']['curr'] + \
        uboat.tanks['quickdive']['Capacity']['curr'] )

    
    # 
    # Вычисляется текущее давление воды на глубине
    # Если  глубина не больше метра - давление не учитывается.
    
    if uboat.c_coord[2] < 0:
        uboat.underwaterpressure = uboat.c_coord[2] ** 2
    elif uboat.c_coord[2] >= -1:
        uboat.underwaterpressure = 0

    #
    # При погружении увеличивается плотность воды и солей, 
    # требуется больше балласта дял продолжения погружения

    if uboat.c_coord[2] in range (-9, 0):
        uboat.seadensity = 0
    elif uboat.c_coord[2] in range (-19, -10):
        uboat.seadensity = 10
    elif uboat.c_coord[2] in range (-29, -20):
        uboat.seadensity = 20
    elif uboat.c_coord[2] in range (-39, -30):
        uboat.seadensity = 30
    elif uboat.c_coord[2] in range (-49, -40):
        uboat.seadensity = 40
    elif uboat.c_coord[2] in range (-59, -50):
        uboat.seadensity = 50
    elif uboat.c_coord[2] in range (-69, -60):
        uboat.seadensity = 60
    elif uboat.c_coord[2] in range (-79, -70):
        uboat.seadensity = 70

    
    if uboat.fixingfloat is False:
        
        # Если принято воды >= необходимой для погружения
        #   если Пл не глубже 150 метров -- увеличить глубину на 1 метр
        if waterloaded > uboat.subsea-1+uboat.seadensity and uboat.c_coord[2] > -150:            
            uboat.c_coord[2] = uboat.c_coord[2]-1
    
        # Если принято воды < необходимой для погружения
        #   Если глубина меньше 0 -- уменьшить глубину на 1 метр
        elif waterloaded < uboat.subsea and uboat.c_coord[2] <= 0:
            uboat.c_coord[2] = uboat.c_coord[2]+1
















# ---------------------------------------------------------
# Глубокое синее море...
# Свалка говнокода крабам.






        #elif uboat.c_coord[2] in range (-10, -110, -10):
            #waterloaded == uboat.subsea - round((uboat.underwaterpressure/9)) and 
            #pass
            
        

        
        # uboat.subsea = uboat.subsea - round((uboat.underwaterpressure/9))

        
        
        
        # if waterloaded == (uboat.subsea - uboat.underwaterpressure)
        
       # - 100 + abs(nn)) and uboat.c_coord[2] in(nn, nn+1):
        
        #uboat.fixingfloat = True
        
        #if waterloaded == (uboat.subsea - 100 + abs(nn)) and uboat.c_coord[2] in(nn, nn+1):
            #uboat.fixingfloat = True
            #uboat.c_coord[2] += 1
            #print('Погружение прекратилось, балласт ' + str(waterloaded) + ' тонн соответствует заданной глубине.')
            
        #else:
            #uboat.fixingfloat = False
            #print('FALSE!', end='-')
            #break






    # 
    # Если в цистернах different1, different2, mainballast, equalizing
    # принято макс., и в quickdive + 10, а глубина -10, то зависнуть на
    # ней до изменения суммы балласта. И ниже каждые 10 м. также
    #
    
    #for nn in range (-10, -110, -10):
    
        #if waterloaded == (uboat.subsea - 100 + abs(nn)) and uboat.c_coord[2] in(nn, nn+1):
            #uboat.fixingfloat = True
            #uboat.c_coord[2] += 1
            #print('Погружение прекратилось, балласт ' + str(waterloaded) + ' тонн соответствует заданной глубине.')
            
        #else:
            #uboat.fixingfloat = False
            #print('FALSE!', end='-')
            #break
        


    



    # принятый балласт
    #uboat.subsea + uboat.tanks['quickdive']['Capacity']['curr']


    #pointfloat = uboat.subsea + (uboat.tanks['quickdive']['Capacity']['curr'] / 5)

    #if uboat.underwaterpressure <= 666 and waterloaded == pointfloat:
        #fixingfloat = True
    #if uboat.underwaterpressure <= 666 and waterloaded == pointfloat + pointfloat:
        #fixingfloat = True
    #else:
        #fixingfloat = False
        
    


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
