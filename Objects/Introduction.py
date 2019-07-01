a = 496
print (id(a))

b= 1729
print (id(b))

b=a
print (id(b)) #You will find that the id of b changed to be the same as that of a

print(id(a)==id(b))
print(a is b)
print(a is None)

r = [2,4,6]
print(r)

s= r
s[1]=17
print(s)
print(r)
print(s is r)

p = [4,7,11]
q= [4,7,11]
print(p ==q)
print(p is q)