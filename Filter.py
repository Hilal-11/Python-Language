
# filter function in python
# filter function in python

data = [2 ,4 ,6 ,7, 1,3, 9 , 11 , 23 , 22 , 29 , 18 , 16]
    # using filter to get all odd elements and even elements
    # using filter to get all elements >= 10 and vice versa

def getOdd(elements) :
    return elements % 2 != 0
odds = list(filter(getOdd , data))
print(odds)

# alternatve
# odds = list(filter(lambda data : data % 2 != 0 , data))
# print(odds)

def getEven(elements) :
    return elements % 2 == 0
evens = list(filter(getEven , data))
print(evens)

# alternatve
# evens = list(filter(lambda data : data % 2 == 0 , data))
# print(evens)

def getElements(elements) :
    return elements >= 10
res = list(filter(getElements , data))
print(res)

def getElements2(elements) :
    return elements <= 10
res2 = list(filter(getElements2 , data))
print(res2)