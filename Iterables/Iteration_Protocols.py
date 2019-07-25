iterable = ['Srping','Summer','Autumn','Winter']
iterator = iter(iterable)

while (True):
    try:
        print(next(iterator))
    except StopIteration:
        print("Reach the end of the list")
        break