#!/usr/bin/python3
# coding: utf-8

# May the Force be with you

# from resources import sea, uboat

# print(uboat.compartments)

'''
people = {'Alice': {'phone': '2341', 'addr': 'Foo drive 23' },
          'Beth':  {'phone': '9102', 'addr': 'Bar street 42'}}
name = 'Alice'          
key = 'phone'
if name in people: 
  print("%s phone is %s" % (name, people[name][key]))
'''

 




tanks = {
    {'differential_1': 
        {
          'name': 'Носовая дифферентная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        }},
    {'differential_2': 
        {
          'name': 'Кормовая дифферентная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        }}
    }

print(tanks['differential_2']['name'])
