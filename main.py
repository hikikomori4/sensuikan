#!/usr/bin/python3
# coding: utf-8

# May the Force be with you

# from resources import sea, uboat

# print(uboat.compartments)


class Tanks(object):
    def differential(self): 
    pass

different1 = differential(self)
different2 = differential(self)

# я не знаю, как мне это лучше применить в классах, чтобы код не потерял читаемость

tanks = {
    'differential_1': 
        {
          'name': 'Носовая дифферентная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },
    'differential_2': 
        {
          'name': 'Кормовая дифферентная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        }
    }

print(tanks['differential_1']['name'])




compartments = [
    {
          'No': 1,
        'name': 'Носовой отсек',
        'desc': 'торпедный, жилой, отсек-убежище.',
       'param': '',
       'truim': '',
       'state': 'отсек в порядке'
    }, 
    {
        'No': 2,
        'name': '',
        'desc': '',
       'param': '',
       'truim': '',
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
       'truim': '',
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
       'truim': '',
       'state': 'отсек в порядке'
    }, 
]

print(compartments[0]['name'])



