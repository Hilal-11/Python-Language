
def scope() :
    username = "Danver"
    print(username)
    def innerScope() :
        name = "Rio"
        print(name)
        print(username)
    innerScope()
    
scope()


x = 99
def scopeIdea(y) :
    return y + x
result = scopeIdea(1)
print(result)

print(x)


def glob():
    global x
    x = 11
glob()
print(x)