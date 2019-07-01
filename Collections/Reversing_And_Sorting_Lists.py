g = [1,11,21,1211,112111]
g.reverse()
print(f'g is {g}')
d= [5,17,41,29,71,149,3299,7,13,67]
d.sort()
print(f'd is now {d}')
d.sort(reverse=True)
print(f'd is now {d}')

h= 'not perple
p = [9,3,1,0]
q=reversed(p)
print(f'q is {q}') #it returns an iterator. to fix that, simply use the contrctur list:
q = list(reversed(p))
print(f'q is {q}')xing do handwriting family where I illegible know doctors'.split()
h.sort(key=len)
print(f'h is now {h}')
joined = ' '.join(h)
print(f'joined = {joined}')

x=[4,9,2,1]
y= sorted(x)
print(f'y is {y}')
