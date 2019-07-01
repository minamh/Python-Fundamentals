import pprint

urls = {'Google':'https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjP_tL_hrHiAhUVJzQIHViMDe0QPAgH', 'Pluralsight':'https://app.pluralsight.com/library/', 'Sixty North':
        'https://sixty-north.com/', 'Microsoft':'https://www.microsoft.com/en-ca/'}

for url in urls:
    print(f'The URL for {url} is {urls[url]}')

names_and_ages = [('Alice',42),('Bob',48),('Charlie',28),('Daniel',33)]
d = dict(names_and_ages)
print(f'The names and ages are {d}')

#Dictionary constructor
phonetic = dict(a='alfa',b='bravo',c='charlie',d='delta',e='echo',f='foxtrot')
print(f'Phonetically: {phonetic}')

#Copying:

e=d.copy()
f = dict(d)
print(f'e is {e}')
print(f'e is d:{e is d}')
print(f'e = d:{e==d}')
print(f'f is {f}')
print(f'f is d:{f is d}')
print(f'f = d:{f==d}')

#Updating:
j = {'John':15,'Mary':23}
d.update(j)
print(f'Names and ages are now {d}')

#If an entry is made with the same key, the value will be updated, for example:

k = {'John':16}
d.update(k)
print(f'Names and ages are now {d}')

#To iterate over only the values:
for age in d.values():
    print(f"Age is {age}")

#Similarly, to iterate over te keys only:
for name in d.keys():
    print(f'Name is {name}')

#To print the pair, we can either follow the method described at the top or:
for key,value in d.items():
    print(f'{key} is {value} years old')

#Membership operators ('in' and 'not in') work on the keys:
print(f'John is in the list: {"John" in d}')
print(f'Luke is in the list: {"Luke" in d}')
print(f'Mary is not in the list: {"Mary" not in d}')
print(f'Peter is not in the list: {"Peter" not in d}')

#Deleting
del d['Mary']
print(f'Names and ages are now {d}')

#dictionary of lists:
m = {'H':[1,2,3],'He':[3,4],'Li':[6,7],'Be':[7,9,10],'B':[10,11],'C':[11,12,13,14]}
print(f'm is: {m}')
m['H'] += [4,5,6,7]
print(f'Now m is: {m}')
m['N'] = [13,14,15]
print(f'm is: {m}')

#Pretty Printing:
print('The pretty print version of m is: ')
pprint.pprint(m)