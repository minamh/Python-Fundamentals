if True:
    print("It's true!")

if False:
    print("It's false!") #won't execute

if bool("eggs"):
    print("Yes please!")

# equivalent to:

if "eggs":
    print("Yes please!")

h=42

if h>50:
    print("Greater than 50")
elif h<20:
    print("Less than 20")
else:
    print("Between 20 and 50")