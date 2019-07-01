p={6,28,496,8128,33550336}

print(f'p is {p}')
print(type(p))

#Constuctor:
e=set()
print(f'e is of type {type(e)}')

#Sets can be created out of lists. They remove duplicates:

s=set([2,4,16,64,4096,65536,262144])
print(f's is {s}')
t=[1,4,2,1,7,9,9]
print(set(t))

#Sets are iterable but the order is arbitrary:

for element in s:
    print(element)

#Memebership:

print(f'1 is in s: {1 in  s}')
print(f'2 is in s: {2 in s}')

#Adding one element at a time(Duplicates are silently ignored):
k = {81,108}
print(f'Now k is {k}')
k.add(54)
print(f'Now k is {k}')
k.add(12)
print(f'Now k is {k}')
k.add(108)
print(f'Now k is {k}')

#Adding multiple elements:
k.update([37,128,97])
print(f'Now k is {k}')

#Removing elements: (If the element is not present, this will produce an error)
k.remove(97)
print(f'Now k is {k}')

#Better way to remove:
k.discard(97)
print(f'Now k is {k}')
k.discard(37)
print(f'Now k is {k}')

#Copying:

j = k.copy()
print(f'Now j is {j}')

#or
m = set(k)
print(f'Now m is {m}')

#Sets are mainly useful in Algebra for uninion operations:
blue_eyes = {'Olivia','Harry','Lilly','Jack','Amelia'}
blonde_hair= {'Harry','Jack','Amelia','Mia','Joshua'}
smell_hcn = {'Harry','Amelia'}
taste_ptc ={'Harry','Amelia','Lilly','Lola'}
o_blood = {'Mia','Joshua','Lilly','Olivia'}
b_blood = {'Amelia','Jack'}
a_blood = {'Harry'}
ab_blood= {'Joshua','Lola'}
print(f'Those who have Blue eyes OR blonde hair are: {blue_eyes.union(blonde_hair)}') #Union
print(f'Those who have Blue eyes AND blonde hair are: {blue_eyes.intersection(blonde_hair)}') #Intersection
print(f'Those who have blonde hair and DO NOT have blue eyes : {blonde_hair.difference(blue_eyes)}') #Difference
print(f'Those who have Blue eyes OR blonde hair BUT NOT BOTH are: {blue_eyes.symmetric_difference(blonde_hair)}') #Symmetric Difference
print(f'Those who can smell hydrogen cyanide are a subset from those who have blonde hair: {smell_hcn.issubset(blonde_hair)}') #Whether it's a subset
print(f'ALL those who can taste PTC can also smell HCN: {taste_ptc.issuperset(smell_hcn)}') #Superset
print(f'No one with O blodd type is also  in the A blood type group: {o_blood.isdisjoint(a_blood)}') #Disjoint