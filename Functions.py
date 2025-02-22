

#   Arbitrary argumants

def addition(*args) :
    sum = 0
    for i in args :
        sum += i
    return sum


sum = addition(10 , 20 , 30 , 40)
print("Sum = ",sum)


# recursion

def factorial(n) :
    if n == 0:
        return 1
    return n * factorial(n-1)

fact = factorial(5)
print(fact)


def printSeries1(n):
    if n == 0:
        return
    print(n,end=" ")
    printSeries1(n-1)
    
def printSeries2(n) :
    if n == 0:
        return
    printSeries2(n-1)
    print(n,end=" ")
    
printSeries1(10)
print("\n")
printSeries2(10)


