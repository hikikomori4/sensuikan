#!/usr/bin/python3
# coding: utf-8


if __name__ == '__main__':
    print('\nМодуль субмарина отдельно не запускается!\n')
    exit(1)




uboatname = 'Тип "С" Средняя'
uboatseries = 'IX-бис'

c_coord = [250,50,0]
c_differ = 0
c_kren = 0

########################################################

canon = {}
canon_ammo ={}
torpedos = {}
torpedos_loaded = {}

########################################################


########################################################

diesel = {
        'state': 'в порядке',
        'rpm': 0
        }

########################################################
#  print(uboat.elmotor['rpm'])

elmotor = {
        'state': 'в порядке',
        'rpm': 0
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
          'state': 'цистерна в порядке' 
        },
    'different2': 
        {
          'name': 'Кормовая дифферентная цистерна',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'цистерна в порядке' 
        },
    'equalizing': 
        {
          'name': 'Уравнительная цистерна',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'цистерна в порядке' 
        },
    'quickdive': 
        {
          'name': 'Цистерна быстрого погружения',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'цистерна в порядке' 
        },
    'mainballast': 
        {
          'name': 'Цистерна главного балласта (ЦГБ)',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'цистерна в порядке'
        },
    'torpedorshaped1': 
        {
          'name': 'Торпедозаместительные цистерны',
          'Capacity': {'curr': 0, 'max': 100},
          'state': 'цистерна в порядке' 
        },
    'torpedorshaped2': 
        {
          'name': 'Торпедозаместительные цистерны',
          'Capacity': {'curr': 0, 'max': 100},
          'state': 'цистерна в порядке' 
        },
    'fuel_tank1': 
        {
          'name': 'Топливная цистерна 1',
          'Capacity': {'curr': 900, 'max': 1000},
          'state': 'цистерна в порядке' 
        },
    'fuel_tank2': 
        {
          'name': 'Топливная цистерна 2',
          'Capacity': {'curr': 900, 'max': 1000},
          'state': 'цистерна в порядке' 
        }
    }

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
    """Конструктор баллонов воздуха высокого давления """

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
    Baloon(300, 300, BALOON_VVD_OK) for i in range(14)
    ]


########################################################

bridge =     {

        'name': 'на ходовом мостике',
        'desc': 'Ходовой мостик служит для управления кораблём в надводном положении, содержит выдвижные устройства.',
       'truim': False,
       'state': 'В порядке'
    }, 

cpt_cabin =  {

        'name': 'в командирской каюте',
        'desc': 'Каюта командира находится во втором отсеке (аккумуляторном), там хранятся карты и секретные документы.',
       'truim': False,
       'state': 'В порядке'
    }, 



########################################################
# Пример вызова извне:
# print(uboat.compartments[2]['desc'])
# print(uboat.compartments[2]['truim']['name'])
 
compartments = [
    {
          'no': None,
        'name': 'в боевой рубке',
        'desc': 'Боевая рубка служит для управления кораблём и дополняет ЦП',
       'param': '',
   'lighthull': False,
       'truim': False,
       'state': 'отсек в порядке'
    }, 
    {
          'no': 1,
        'name': 'в носовом отсеке',
        'desc': 'Первый отсек-убежище: торпедный, жилое помещение для рядового состава.',
       'param': '',
   'lighthull': (tanks['torpedorshaped1'], tanks['different1'],baloon_vvd[0],baloon_vvd[1]),
       'truim': '',
       'state': 'отсек в порядке'
    }, 
    {
        'no': 2,
        'name': 'в аккумуляторном 2-м отсеке',
        'desc': 'Второй отсек: аккумуляторный, 62 элемента носовой группы ' +
                'аккумуляторных батарей, каюта командира, жилые помещения ' +
                'офицерского состава.',
       'param': '',
   'lighthull': (tanks['fuel_tank1'],baloon_vvd[2], baloon_vvd[3]),
       'truim': (battery1),
       'state': 'отсек в порядке'
    }, 
    {
        'no': 3,
        'name': 'в центральном посту',
        'desc': 'Третий отсек-убежище: центральный пост (ЦП), над отсеком ' +
                'расположена боевая рубка и ограждение выдвижных устройств.',
       'param': '',
   'lighthull': (baloon_vvd[4], baloon_vvd[5]),
       'truim': '',
       'state': 'отсек в порядке'
    }, 
    {
        'no': 4,
        'name': 'в аккумуляторном 4-м отсеке',
        'desc': 'Четвёртый отсек: аккумуляторный, 62 элемента кормовой ' +
                'группы аккумуляторных батарей, жилые помещения старшин.',
       'param': '',
   'lighthull': (tanks['fuel_tank2'], baloon_vvd[6], baloon_vvd[7]),
       'truim': (battery2),
       'state': 'отсек в порядке'
    }, 
    {
        'no': 5,
        'name': 'в дизельном отсеке',
        'desc': 'Пятый отсек: дизельный.',
       'param': '',
   'lighthull': (baloon_vvd[8], baloon_vvd[9]),
       'truim': diesel,
       'state': 'отсек в порядке'
    }, 
    {
        'no': 6,
        'name': 'в электромоторном отсеке',
        'desc': 'Шестой отсек: электромоторный.',
       'param': '',
   'lighthull': (baloon_vvd[10],baloon_vvd[11]),
       'truim': elmotor,
       'state': 'отсек в порядке'
    }, 
    {
        'no': 7,
        'name': 'в кормовом отсеке',
        'desc': 'Седьмой отсек-убежище: торпедный, жилое помещение для рядового личного состава.',
       'param': '',
   'lighthull': (tanks['torpedorshaped2'], tanks['different2'],baloon_vvd[12],baloon_vvd[13]),
       'truim': '',
       'state': 'отсек в порядке'
    }, 
]


########################################################
# ПЛ со всем содержимым



       
hull = {
        'bridge': bridge,
        'light': tanks['mainballast'],
       'strong': compartments}





