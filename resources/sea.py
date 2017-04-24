#!/usr/bin/python3
# coding: utf-8

import sys
import csv

from resources import uboat

    
filename = './resources/sea.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
      # sea = list(reader)  # занесение csv в [список]
        sea = tuple(reader) # занесение csv в (кортеж)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}' \
        .format(filename, reader.line_num, e))


# x, y, surface, bottom
#print(sea[0])
#print(sea[100])

# Глубокое синее море...



#polygon1 =()
#for coord in sea:
    
    #coordprev = str(coord)
    #next
    #if coordprev[2] == str(coord[2]):
        #polygon1 += tuple(coordprev)


#print(polygon1)
    
    #if int(coord[0]) < uboat.c_coord[0]:
        #print(uboat.c_coord[0] - int(coord[0]))
    #elif int(coord[0]) > uboat.c_coord[0]:
        #print(int(coord[0]) - uboat.c_coord[0])








if __name__ == '__main__':
    print('Модуль описывает игровое пространство, и отдельно не запускается!')

