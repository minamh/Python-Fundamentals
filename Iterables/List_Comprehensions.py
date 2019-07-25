Words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
print(Words)

'''To generate an a list comprehension, the syntax is [expression(item) for item in iterable] Fore mexample:'''

print([len(word) for word in Words])
print([len(word) for word in Words if len(word)>3])

#This is the same as doing this:
lengths = []
for word in Words:
    lengths.append(len(word))

print(lengths)