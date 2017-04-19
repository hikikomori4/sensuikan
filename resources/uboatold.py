#!/usr/bin/python3
# coding: utf-8

#if __name__ == '__main__':
#    print('\nМодуль субмарина отдельно не запускается!\n')
#    exit(1)



uboatname = 'Тип "С" Средняя'
uboatseries = 'IX-бис'


  
       


########################################################
# Пример вызова извне:
#print(uboat.tanks['mainballast']['name'])
#print(uboat.tanks['mainballast']['Capacity']['max'])

tanks = {
    'different1': 
        {
          'name': 'Носовая дифферентная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'different2': 
        {
          'name': 'Кормовая дифферентная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'equalizing': 
        {
          'name': 'Уравнительная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'quickdive': 
        {
          'name': 'Цистерна быстрого погружения',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'mainballast': 
        {
          'name': 'Цистерна главного балласта (ЦГБ)',
          'Capacity': {'curr': 0, 'max': 1000},
          'state': 'цистерна в порядке'
        },
    'torpedo': 
        {
          'name': 'Торпедозаместительные цистерны',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'ringshaped': 
        {
          'name': 'Цистерны кольцевого зазора',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'fuel_tank1': 
        {
          'name': 'Топливная цистерна 1',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'fuel_tank2': 
        {
          'name': 'Топливная цистерна 2',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        }
    }


print(tanks['mainballast']['name'])
print(tanks['mainballast']['Capacity']['max'])



########################################################


compartments = [
    {
          'No': 0,
        'name': 'Боевая рубка',
        'desc': '',
       'param': '',
       'truim': False,
       'state': 'отсек в порядке'
    }, 
    {
          'No': 1,
        'name': 'Носовой отсек',
        'desc': 'торпедный, жилой, отсек-убежище.',
       'param': '',
       'truim': tanks['different1'],
       'state': 'отсек в порядке'
    }, 
    {
        'No': 2,
        'name': '',
        'desc': '',
       'param': '',
       'truim': tanks['fuel_tank1'],
       'state': 'отсек в порядке'
    }, 
    {
        'No': 3,
        'name': 'Центральный пост',
        'desc': 'отсек-убежище',
       'param': '',
       'truim': '',
       'state': 'отсек в порядке'
    }, 
    {
        'No': 4,
        'name': '',
        'desc': '',
       'param': '',
       'truim': tanks['fuel_tank2'],
       'state': 'отсек в порядке'
    }, 
    {
        'No': 5,
        'name': '',
        'desc': '',
       'param': '',
       'truim': '',
       'state': 'отсек в порядке'
    }, 
    {
        'No': 6,
        'name': '',
        'desc': '',
       'param': '',
       'truim': '',
       'state': 'отсек в порядке'
    }, 
    {
        'No': 7,
        'name': 'Кормовой отсек',
        'desc': 'Торпедный, жилой, отсек-убежище',
       'param': '',
       'truim': tanks['different2'],
       'state': 'отсек в порядке'
    }, 
]


########################################################
# ПЛ со всем содержимым

       
hull = {
        'light': tanks['mainballast'],
       'strong': compartments}

