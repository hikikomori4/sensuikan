#!/usr/bin/python3
# coding: utf-8

import os
import sys
import random
import csv

os.system('clear')

filename = 'sea.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    
    try:
      # sea = list(reader)  # занесение csv в [список]
        sea = tuple(reader) # занесение csv в (кортеж)
        

            
    except csv.Error as e:
        sys.exit('file {}, line {}: {}' \
        .format(filename, reader.line_num, e))


# print(sea)
# id, x, y, surface, bottom, status

print(sea[0])
print(sea[100])
