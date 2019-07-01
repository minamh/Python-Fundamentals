#Finding elements:
w = "the quick brown fox jumps over the lazy dog".split()
print(w)
i = w.index("fox")
print(i)
#e=w.index("cat")
#print(e)

#Count occurrences:
count=w.count("the")
print(f'count is {count}')

#Membership:
print(37 in [1,2,3,4,5,37])
print(37 not in [1,2,3,4,37])

#Removing by index:
u = "jackdaws love my big sphinx of quarts".split()
print(u)
del u[3]
print(u)

#Remove by index:
u.remove("my")
print(u)

#or by both:
del u[u.index("jackdaws")]
print(u)

#insert items:
a = "I accidentally the whole universe".split()
print(a)
a.insert(2,'destroyed')
print(a)
b= ' '.join(a)
print(b)