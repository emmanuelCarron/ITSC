import datetime

def is_monday():
    today = datetime.datetime.now()
    return today.weekday() == 0

def is_twesday():
    today = datetime.datetime.now()
    return today.weekday() == 1

def is_wednesday():
    today = datetime.datetime.now()
    return today.weekday() == 2

def is_thursday():
    today = datetime.datetime.now()
    return today.weekday() == 3

def is_friday():
    today = datetime.datetime.now()
    return today.weekday() == 4

def is_saturday():
    today = datetime.datetime.now()
    return today.weekday() == 5

def is_sunday():
    today = datetime.datetime.now()
    return today.weekday() == 6

if __name__ == '__main__':
    if is_monday():
        print('hola lunes!')
    else:
        print('hola NO lunes!')
