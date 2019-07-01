from math import log

def convert (s):
    '''Convert to an integer'''
    try:
        x = int (s)
        print(f'Conversion succeeded. X= {x}')
    except (ValueError, TypeError) as ex:
        print('Exception caught')
        return -1

def string_log(s):
    v = convert(s)
    return log(v)

#The main point here is to show that even an invalid value of S can be caught in the exception, it will break the log as it doesn't accept -ve values
string_log('Mina')