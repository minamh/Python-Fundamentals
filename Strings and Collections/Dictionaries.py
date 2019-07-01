telephoneDirectory = {'alice':'123-456-7890', 'bob':'0987654321','eve':'1029384756'}
print(telephoneDirectory['alice'])
print(telephoneDirectory)
telephoneDirectory['alice'] = '123-456-7899'
print(telephoneDirectory)
telephoneDirectory['charles']='5463728190'
print(telephoneDirectory)
print(telephoneDirectory['notfound'])

#To create an empty dictionary:
emptyDictionary = {}