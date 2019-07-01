import math

print(math.sqrt(81))

print(math.factorial(5))
print(math.factorial(6))

n = 5
k = 3
print((math.factorial(5))/((math.factorial(3))*math.factorial(n-k)))

#Since we know it will always return an integer, we can change it to  integer division by addin double slashes instead of one

print((math.factorial(5))//((math.factorial(3))*math.factorial(n-k)))

print(len(str(math.factorial(100))))