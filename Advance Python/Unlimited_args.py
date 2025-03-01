

# def add (a  , b) :
#     return a + b

# print(add(10 , 20))

# def add(*args) :
#     sum = 0
#     for i in args :
#         sum += i
#     return sum
    
# print(add(1 , 4 , 7 , 8))


def add(*values) :
    sum = 0
    for i in values:
        sum += i
    return sum
    
print(add(1 , 4 , 6 , 9  , 8))