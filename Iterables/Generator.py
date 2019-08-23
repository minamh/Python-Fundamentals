#This is how a generator is defined which is similar to a list comprehension
million_squares= (x*x for x in range (1,1000001))

print(next(million_squares))
print(next(million_squares))
print(next(million_squares))