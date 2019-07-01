count  = 0

def show_count():
    global count
    print(f'count = {count}')

def set_count(c):
    count = c

show_count()

set_count(5)

show_count() #The Variable count doesn't change. The function needs to be instructed that we're referring to the global one.

def set_count2(c):
    global count
    count = c

show_count()

set_count2(5)

show_count()