#!/usr/bin/python3
# coding: utf-8



  
TANK_ST_OK = 0
TANK_ST_SMOKE = 1      
TANK_ST_FIRE  = 2
TANK_ST_WATER = 3


class Tank:
    """Конструктор топливных и балластных цистерн """

    def __init__(self, shortid, name, capacity, taken, condition ):
        self.shortid = shortid
        self.name = name
        self.capacity = capacity
        self.taken = taken
        self.condition = condition
        
        shortid = {shortid:{name,capacity,taken,condition}}

    def __repr__(self):
        return '{} {} {} {} {}\n' \
        .format(self.shortid, self.name, self.capacity, self.taken, self.condition)




tanks = {
     Tank('different1',
         'Носовая дифферентная цистерна', 1000, 0, TANK_ST_OK)

}


# Пример вызова:
# print(tanks)


tanks2 = {
    'different2': 
        {
          'name': 'Кормовая дифферентная цистерна',
          'Capacity': 1000,
          'state': 'цистерна в порядке' 
        },

}





tanks3 = {

    'equalizing': {Tank('Уравнительная цистерна', 1000, 0, TANK_ST_OK)},

}


print(vars()) 

# print(tanks['different1']['name'])

# print(tanks['different1']['Capacity']['max'])



