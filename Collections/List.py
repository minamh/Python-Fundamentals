#spli method returns a list:
s = "Show how to index into sequences".split()
print(s)

#Indexing elements from the end:

#accessig the fifth element from the end:
print(s[-5])

#slicing a list:
subList = s[1:4]

print(f'The sub-list is {subList}')

#An example of an opend ended slicing:

subList2=s[3:]

print(f'The open-ended sub list is{subList2}')

#An Example of a sublist with only an ending:

subList3 = s[:3]

print(f'The close-ended sublist is {subList3}')

#This is how to make a hard-copy of the list:
shallowCopy = s[:]
print(shallowCopy)
print(shallowCopy is s)
print(shallowCopy == s)
print(f's[0] is hardCopy[0]: {s[0] is shallowCopy[0]}')
s[1]='change'
print(s)
print(shallowCopy)
#another way:
copyList=s.copy()
copyList[2]='New'
print(copyList)
print(s)
#yet another way (The mother of all: List constructor):
constructedList=list(s)
constructedList [0]='constructed'
print(constructedList)
print(s)