from math import factorial
'''Set Comprehensions are the same as set except we use curly braces except squared ones'''

#Syntax is {expression (item) for item in iterable}
Set_Comprehension = {len(str(factorial(x))) for x in range(20)}
print(Set_Comprehension)