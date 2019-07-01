print(len("llanfairpwllgwllgwy"))

#Example of concatination

a= 'New'
b='found'
c='land'
d = a+b+c
print(d)

colors = ';'.join(['red','blue','green','yellow'])
print(colors)
print(colors.split(';'))

#So another way to concatinate, you can invoke join on empty text:
bigWord=''.join(['other ','smaller ', 'words.'])
print(bigWord)

#Break it down

print('hopaba2ayalla'.partition('ba2a'))
departure, separator, arrival = 'cai:yvr'.partition(':')
print(departure)
print(arrival)

#format
print('The age of {0} is {1}'.format('jim','32'))
#or
print('The age of {name} is {age}'.format(name='jim',age='32'))