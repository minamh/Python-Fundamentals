# def convert (s):
#     '''Convert to an integer'''
#     try:
#         x = int (s)
#         print(f'Conversion succeeded. X= {x}')
#     except ValueError:
#         x=-1
#         print(f"Conversion Failed!(Value Error) Can't convert {s} to integer")
#     except TypeError:
#         x=-1
#         print(f"Conversion Failed!(Type Error) Can't convert {s} to integer")
#     return x

#A better way to define convert:

def convert (s):
    '''Convert to an integer'''
    try:
        x = int (s)
        print(f'Conversion succeeded. X= {x}')
    except (ValueError, TypeError) as ex:
        x=-1
        print(f"Conversion Failed!{str (type(ex))[7:str (type(ex)).find('>')]} Can't convert {s} to integer")
    return x

convert('34')
convert('Giraffe')
#How about this: (Initially it will fail.Add a TypeErrpor exception
convert([4,5,6])
