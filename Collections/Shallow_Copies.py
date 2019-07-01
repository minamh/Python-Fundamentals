a=[[1,2],[3,4]]
b=a[:]
print(f'a is b: {a is b}')
print(f'a[0] is b[0]: {a[0] is b[0]}')
a[0]=[8,9]
print(f'a is: {a}')
print(f'b is: {b}')
a[1].append(5)
print(f'a is b: {a is b}')
print(f'a[0] is b[0]: {a[0] is b[0]}')
print(f'a is: {a}')
print(f'b is: {b}')