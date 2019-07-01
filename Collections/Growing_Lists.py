#lists concatination:
m = [2,1,3]
n = [4,7,11]
k = m + n
print(f'k is {k}')
k += [18,29,47]
print(f'now k ={k}')
k.extend([76,129,199])
print(f'now k ={k}')