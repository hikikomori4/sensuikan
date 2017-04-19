


# print(uboat.compartments[0]['name'])
# print(uboat.compartments[1]['truim'])
#print(uboat.compartments[1])

# print(tanks['different1']['name'])
# print(tanks['different1'])


# print(uboat.hull)
print(uboat.tanks['mainballast']['Capacity']['curr'])
print(uboat.tanks['mainballast']['Capacity']['max'])


'''
actions = {
    'принять в ЦГБ 2Т воды': task_tank,
    '': task_,
    '': task_,
    '': task_,
    '': task_,
    '': task_,
    '': task_,
    '': task_,
    '': task_,
    '': task_,
    'выход': task_exit
    }
    
    

if __name__== '__main__':
    show_menu()

    while True:
        cmd = input('\x1b\x5b\x37\x6d1\x1b\x5b\x30\x6d-List \x1b\x5b\x37\x6d2\x1b\x5b\x30\x6d-Add \x1b\x5b\x37\x6d3\x1b\x5b\x30\x6d-Edit \x1b\x5b\x37\x6d4\x1b\x5b\x30\x6d-Del \x1b\x5b\x37\x6d5\x1b\x5b\x30\x6d-Terminate \x1b\x5b\x37\x6d6\x1b\x5b\x30\x6d-Resume \x1b\x5b\x37\x6dm\x1b\x5b\x30\x6denu \x1b\x5b\x37\x6dq\x1b\x5b\x30\x6duit  ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('\nНеизвестная команда\n')

'''
