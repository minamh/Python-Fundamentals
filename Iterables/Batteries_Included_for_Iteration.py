from itertools import islice, count, chain
from math import sqrt

def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(sqrt(x))+ 1):
        if x%i==0:
            return False
    return True


#islice(all_primes,1000)

thousand_primes=islice((x for x in count() if is_prime(x)),1000)

print(list(thousand_primes))

print (any(is_prime(x) for x in range(1328,1361)))

sunday = [12,14,15,15,17,21,22,22,23,22,20,18]
monday = [13,14,14,14,16,20,21,22,22,21,19,17]

for mon,sun in zip(monday,sunday):
    print(f"The average temperature is {(mon+sun)/2}")

tuesday= [2,2,3,7,9,10,11,12,10,9,8,8]

all_temps = chain(sunday, monday,tuesday)
for temps in all_temps:
    print(temps)