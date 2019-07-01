#To leave the exceopt block empty, you can use the keyword pass:
def convert (s):
    '''Convert to an integer'''
    try:
        x = int (s)
        print(f'Conversion succeeded. X= {x}')
    except (ValueError, TypeError) as ex:
        pass

convert('33')
convert('Giraffe') #nothing happens and no error is raised