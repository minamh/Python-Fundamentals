a = range (5)
print(a)

for i in range (5):
    print(i)

b = range (5,10)
print(b)
print(list(b))

c = range(0,10,2)
print(c)
print(list(c))

#This produces a tuple:
p = [1,2,3,5,6,7,8]
for s in enumerate(p):
    print(s)

for i,v in enumerate(p):
    print(f"i = {i}, v = {v}")