from math import log

def convert (s):
    '''Convert to an integer'''
    try:
        x = int (s)
        print(f'Conversion succeeded. X= {x}')
    except (ValueError, TypeError) as ex:
        print(f'Exception caught: {str(ex)}')
        raise

def string_log(s):
    v = convert(s)
    return log(v)

string_log('Mina')