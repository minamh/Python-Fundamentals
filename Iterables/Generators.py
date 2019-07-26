def gen123():
    yield 1
    yield 2
    yield 3
    return

g = gen123()

print(g)
print(next(g))

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    return
k = gen246()

print(next(k))
print(next(k))
print(next(k))