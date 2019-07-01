#Example of string conctenation
concatinatedString = "First""Second"
print(concatinatedString)

text= """This is a
multiline
string"""
print(text)

#Another way to do it
text2 = "This string \nspans \nmultiple lines. "
print(text2)

#This is a raw string

rawString = r"C:\Users\minah\OneDrive\Pictures"
print(rawString)

#Strings are sequence variables. So we can do this:
variable = str(7.897)
print(variable[2])

#There are no characters in Python
variable2='s'
print(type(variable2))

#Different string operations:
stringVariable = "oslo"
print(stringVariable.capitalize())
print(stringVariable.upper())
print(stringVariable.lower())

listOfText = text.split()
print(listOfText)
print(type(listOfText))