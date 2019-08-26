"""Model for aircraft flights"""

class Flight:
    def number (self):
        return"SN060"

f=Flight()
print(f.number())
#same as :
print(Flight.number(f))