m = [9,15,24]

def modify(k):
    k.append(39)
    print(f'k = {k}')

modify(m)

f = [14,23,37]

def replace (g):
    g = [17,28,45]
    print(f'g = {g}')

replace(f)
print(f'f = {f}')
#The original f list is still the same and g is a new list
#To replace f by g, we need to modify the contents like this:

def replace_contents(g):
    g[0]= 17
    g[1]=28
    g[2]=45
    print(f'g = {g}')

#now make the function call and print f

replace_contents(f)
print(f'f = {f}')

def f(d):
    return d

c = [6,10,16]
e=f(c)
print(e is c)
