#!/usr/bin/python3
# coding: utf-8


TANK_COND_OK = 0
TANK_COND_ERROR = 1

class Tank:
    """Конструктор топливных и балластных цистерн """

    def __init__(self, name, capacity, taken, condition ):
        self.name = name
        self.capacity = capacity
        self.taken = taken
        self.condition = condition

    def __repr__(self):
        return '{}  {} {} {}\n' \
        .format(self.name, self.capacity, self.taken, self.condition)

# Создание 1й цистерны с помощью переменной.
different1 = Tank('Носовая дифферентная цистерна', 1000, 0, TANK_COND_OK)
print (different1.name, different1.capacity, different1.taken, different1.condition)

# Создание всех цистерн с помощью списка.
tanks = [
    Tank('Носовая дифферентная цистерна', 1000, 0, TANK_COND_OK),
    Tank('Кормовая дифферентная цистерна', 1000, 0, TANK_COND_OK),
    Tank('Уравнительная цистерна', 1000, 0, TANK_COND_OK),
    Tank('Цистерна быстрого погружения', 1000, 0, TANK_COND_OK),
    Tank('Цистерна главного балласта (ЦГБ)', 1000, 0, TANK_COND_OK),
    Tank('Торпедозаместительные цистерны', 1000, 0, TANK_COND_OK),
    Tank('Цистерны кольцевого зазора', 1000, 0, TANK_COND_OK),
    Tank('Топливная цистерна 1', 1000, 0, TANK_COND_OK),
    Tank('Топливная цистерна 2', 1000, 0, TANK_COND_OK)
]

print(tanks[1].name, tanks[1].capacity, tanks[1].taken, tanks[1].condition)
print('\n',tanks,'\n')

print('')

