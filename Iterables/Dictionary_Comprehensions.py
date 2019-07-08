import pprint
import os
import glob
#Syntax is {key:value for item(key,value in the following iterable) in iterable.items()}

country_to_capital = {'United Kingdom':'London','Brazil':'Brazilia','Morocco':'Rabat','Sweden':'Stockholm'}
capital_to_country = {capital:country for country,capital in country_to_capital.items()}

pprint.pprint(capital_to_country)

words = ["hi","hello","foxtrot","hotel"]
first_letter = {x[0]:x for x in words}
pprint.pprint(first_letter)

python_files = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob(pathname='*.py',recursive=True)}
pprint.pprint(python_files)