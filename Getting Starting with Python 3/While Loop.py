c=5
while (c!=0):
    print(c)
    c-=1

#same as:
c=5
while c:
    print(c)
    c-=1

while True:
    response = input("7ot el rakam yah: ")
    if int(response)%7==0:
        break
