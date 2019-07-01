import time

def banner (message, border = '-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue")
banner("Sun, Moon and Stars","*")
#Another way to make the function call:
banner("Sun, Moon and Stars",border="*")
banner(border=".",message="Hello from Earth!")

print(time.ctime())

def show_default(arg = time.ctime()):
    print(arg)

show_default()
#notice what happens if we wait a bit:
time.sleep(2)
show_default()
#time is the same. It hasn't progressed. To fix this, simply move the argument into the function body like this:

def show_default2():
    arg = time.ctime()
    print(arg)

show_default2()
#notice what happens if we wait a bit:
time.sleep(2)
show_default2()