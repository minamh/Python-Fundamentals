g =open('wasteland.txt',mode='rt', encoding='utf-8')
print(g.read(32))
print(g.read())
print(g.read())
#Go back to the begining of the file
g.seek(0)
print(g.readline())
print(g.readline())
print(g.readline())

g.seek(0)

#Read all lines into a list:
lines = g.readlines()
print(lines)

#Always remember to close files:
g.close()