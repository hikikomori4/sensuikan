#!/usr/bin/python3
# coding: utf-8

import random

if __name__ == '__main__':
    print('\nМодуль субмарина отдельно не запускается!\n')
    exit(0)


uboatname = 'Тип "С" Средняя'
uboatseries = 'IX-бис'

c_coord = [250,50,1]
c_differ = 0
c_kren = 0
v_rule = 0
h_rule1 = 0
h_rule2 = 0
speed  = 0

waterloaded = 0


########################################################

canon = {}
canon_ammo ={}
torpedos = {}
torpedos_loaded = {}

########################################################

# Пример вызова извне:
# print(uboat.engines['diesel1']['state'])



########################################################

engines = {
    'diesel1': 
        {
        'state': 'в порядке',
        'rpm': 0
        },
    'diesel2': 
        {
        'state': 'в порядке',
        'rpm': 0
        },
    'electro1': 
        {
        'state': 'в порядке',
        'rpm': 0
        },
    'electro2': 
        {
        'state': 'в порядке',
        'rpm': 0
        }
    }


########################################################

battery_cell_v = 2.1
battery_cell_h = 3000


battery1 = [battery_cell_v for i in range(62)]
battery2 = [battery_cell_v for i in range(62)]





########################################################
# Пример вызова извне:
#print(uboat.tanks['mainballast']['name'])
#print(uboat.tanks['mainballast']['Capacity']['max'])

tanks = {
    'different1': 
        {
          'name': 'Носовая дифферентная цистерна',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'исправна' 
        },
    'different2': 
        {
          'name': 'Кормовая дифферентная цистерна',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'исправна' 
        },
    'equalizing': 
        {
          'name': 'Уравнительная цистерна',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'исправна' 
        },
    'quickdive': 
        {
          'name': 'Цистерна быстрого погружения',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'исправна' 
        },
    'mainballast': 
        {
          'name': 'Цистерна главного балласта (ЦГБ)',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'исправна'
        },
    'torpedorshaped1': 
        {
          'name': 'Торпедозаместительные цистерны',
          'Capacity': {'curr': 0, 'max': 100},
          'state': 'исправна' 
        },
    'torpedorshaped2': 
        {
          'name': 'Торпедозаместительные цистерны',
          'Capacity': {'curr': 0, 'max': 100},
          'state': 'исправна' 
        },
    'fuel_tank1': 
        {
          'name': 'Топливная цистерна 1',
          'Capacity': {'curr': 900, 'max': 1000},
          'state': 'исправна' 
        },
    'fuel_tank2': 
        {
          'name': 'Топливная цистерна 2',
          'Capacity': {'curr': 900, 'max': 1000},
          'state': 'исправна' 
        }
    }



cruiser = tanks['quickdive']['Capacity']['max']

position = tanks['mainballast']['Capacity']['max'] \
            + tanks['different1']['Capacity']['max'] \
            + tanks['different2']['Capacity']['max'] \

subsea = tanks['mainballast']['Capacity']['max'] \
            + tanks['different1']['Capacity']['max'] \
            + tanks['different2']['Capacity']['max'] \
            + tanks['equalizing']['Capacity']['max'] 


PSCOPE_DEEP = -10
SAFE_DEEP = -25
WORK_DEEP = -70
MAX_DEEP = -100
CALC_DEEP = -120


########################################################
#
# Баллоны запаса ВВД
#
########################################################
'''
Вызов извне:
print(uboat.baloon_vvd[1].capacity, uboat.baloon_vvd[1].taken, uboat.baloon_vvd[1].condition)
print('\n',uboat.baloon_vvd,'\n')
'''

class Baloon:
    """Конструктор баллонов воздуха высокого давления (ВВД) """

    def __init__(self, capacity, taken, condition ):
        self.capacity = capacity
        self.taken = taken
        self.condition = condition
        

    def __repr__(self):
        return '{} {} {}\n' \
        .format(self.capacity, self.taken, self.condition)
        


# Создание всех баллонов ВВД генератором в списке, методом класса.

BALOON_VVD_OK = 0
BALOON_VVD_BROKE = 1

baloon_vvd = [
    Baloon(3000, 3000-random.randrange(100), BALOON_VVD_OK) for i in range(14)
    ]

 


########################################################

bridge =     {

        'name': 'ходовом мостике',
        'desc': 'Ходовой мостик служит для управления кораблём в надводном положении, содержит выдвижные устройства.',
       'truim': False,
       'state': 'всё исправно'
    }, 

cpt_cabin =  {

        'name': 'командирской каюте',
        'desc': 'Каюта командира находится во втором отсеке (аккумуляторном), там хранятся карты и секретные документы.',
       'truim': False,
       'state': 'всё исправно'
    }, 



########################################################
# Пример вызова извне:
# print(uboat.compartments[2]['desc'])
# print(uboat.compartments[2]['truim']['name'])
 
compartments = [
    {
          'no': None,
        'name': 'боевой рубке',
        'desc': 'Боевая рубка служит для управления кораблём и дополняет ЦП',
       'param': '',
   'lighthull': False,
       'truim': False,
       'state': 'всё исправно'
    }, 
    {
          'no': 1,
        'name': 'носовом отсеке',
        'desc': 'Первый отсек-убежище: торпедный, жилое помещение для рядового состава.',
       'param': '',
   'lighthull': (tanks['torpedorshaped1'], tanks['different1'],baloon_vvd[0],baloon_vvd[1]),
       'truim': '',
       'state': 'всё исправно'
    }, 
    {
        'no': 2,
        'name': 'аккумуляторном 2-м отсеке',
        'desc': 'Второй отсек: аккумуляторный, 62 элемента носовой группы ' +
                'аккумуляторных батарей, каюта командира, жилые помещения ' +
                'офицерского состава.',
       'param': '',
   'lighthull': (tanks['fuel_tank1'],baloon_vvd[2], baloon_vvd[3]),
       'truim': (battery1),
       'state': 'всё исправно'
    }, 
    {
        'no': 3,
        'name': 'центральном посту',
        'desc': 'Третий отсек-убежище: центральный пост (ЦП), над отсеком ' +
                'расположена боевая рубка и ограждение выдвижных устройств.',
       'param': '',
   'lighthull': (baloon_vvd[4], baloon_vvd[5]),
       'truim': '',
       'state': 'всё исправно'
    }, 
    {
        'no': 4,
        'name': 'аккумуляторном 4-м отсеке',
        'desc': 'Четвёртый отсек: аккумуляторный, 62 элемента кормовой ' +
                'группы аккумуляторных батарей, жилые помещения старшин.',
       'param': '',
   'lighthull': (tanks['fuel_tank2'], baloon_vvd[6], baloon_vvd[7]),
       'truim': (battery2),
       'state': 'всё исправно'
    }, 
    {
        'no': 5,
        'name': 'дизельном отсеке',
        'desc': 'Пятый отсек: дизельный.',
       'param': '',
   'lighthull': (baloon_vvd[8], baloon_vvd[9]),
       'truim': (engines['diesel1'],engines['diesel2']),
       'state': 'всё исправно'
    }, 
    {
        'no': 6,
        'name': 'электромоторном отсеке',
        'desc': 'Шестой отсек: электромоторный.',
       'param': '',
   'lighthull': (baloon_vvd[10],baloon_vvd[11]),
       'truim': (engines['electro1'],engines['electro2']),
       'state': 'всё исправно'
    }, 
    {
        'no': 7,
        'name': 'кормовом отсеке',
        'desc': 'Седьмой отсек-убежище: торпедный, жилое помещение для рядового личного состава.',
       'param': '',
   'lighthull': (tanks['torpedorshaped2'], tanks['different2'],baloon_vvd[12],baloon_vvd[13]),
       'truim': '',
       'state': 'всё исправно'
    }, 
]


########################################################
# ПЛ со всем содержимым



       
hull = {
        'bridge': bridge,
        'light': tanks['mainballast'],
       'strong': compartments}





