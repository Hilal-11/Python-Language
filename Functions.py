import math

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

print("\n\n")

# basic functions syntax

def getSquare(n) :
    return n ** 2

def getCube(n) :
    return n * n * n

print(getSquare(2))
print(getSquare(4))

print(getCube(2))
print(getCube(4))


# function return multiple values
def get_square_cude(n) :
    square = n ** 2
    cube = n * n * n
    return (square , cube)

print(get_square_cude(5))
# function default parameters
def get_square_cude(n = 1) :
    square = n ** 2
    cube = n * n * n
    return (square , cube)

print(get_square_cude())


# given a radius return both ( area , circumference ) of a giver radius
print("\n")

def get_ares_circumfrence(radius = 1) : # default value = 1
    area = math.pi * radius*radius
    circumfrence = 2 * math.pi * radius
    return (area , circumfrence)
area , circumfrence = get_ares_circumfrence(3)
print("Area = ", round(area , 3))
print("circumfrence = ", round(circumfrence , 3))
