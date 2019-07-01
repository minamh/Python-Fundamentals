t =("Norway",4.953,3)

print(t)

print(t[0])

print(len(t))

for item in t:
    print(item)

t = t+(338186.0 , 265e9)

print(t)

t = t*3

print(t)

#We can have nested tuples:
a = ((220, 284),(1184,1210),(2620,2924),(5020,5564))
print(a[2])
print(a[2][1])

#Empty Tuple:
e= ()
print(type(e))

p = (1,1,1,4,6,19)

def minmax(items):
    return min(items), max(items)
print(minmax(p))

#another way to do it:
lower,upper = minmax(p)
print(lower)
print(upper)

print(tuple("Carmichael"))

print (5 in p)
print (1 in p)
print(5 not in p)