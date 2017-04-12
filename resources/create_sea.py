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
        # занесение csv в [ список\list ]
        sea = list(reader)
        

            
    except csv.Error as e:
        sys.exit('file {}, line {}: {}' \
        .format(filename, reader.line_num, e))


print(sea)
