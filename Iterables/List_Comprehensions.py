Words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
print(Words)

'''To generate an a list comprehension, the syntax is [expression(item) for item in iterable] Fore mexample:'''

print([len(word) for word in Words])

#This is the same as doing this:
lengths = []
for word in Words:
    lengths.append(len(word))

print(lengths)