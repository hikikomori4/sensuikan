#!/usr/bin/python3
# coding: utf-8

import sqlite3


SQL_SELECT = '''
    SELECT
        id, x, y, surface, bottom, status
    FROM
        sea
    '''


def dict_build(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_build
    return conn


def initialize(conn):
    with conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS sea (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                x INTEGER NOT NULL,
                y INTEGER NOT NULL,
                surface INTEGER NOT NULL,
                bottom INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'None'
            )
        ''')


def task1(task):
    print('{task[id]} - {task[x]} - {task[y]} - {task[surface]} - {task[bottom]} - {task[status]}'.format(task=task))



def task_add(conn):
    cursor = conn.execute('''
    INSERT INTO scheduler (id, title, body, time) 
    VALUES (?,?,?,?)
    ''', (
    int(input('Введите № события: ')),
    input('Введите его название: '),
    input('Введите текст: '),
    input('Введите дату\время (гггг-мм-дд чч:мм): ')
         )
    )
    return cursor.lastrowid


def cell_add(conn):
    cursor = conn.execute('''
    INSERT INTO sea (id, x, y, surface, bottom, status) 
    VALUES (?,?,?,?,?,?)
    ''', (0,0,0,0,0,''))
    return cursor.lastrowid











if __name__ == '__main__':
    print('Модуль описывает игровое пространство, и отдельно не запускается!')

