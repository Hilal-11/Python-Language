
# def myGenerator(n) :
#     for x in range(n) :
#         yield x ** 3
        
# values = myGenerator(9000000)
 
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

print("\n")

# def myGenerator2(n) :
#     for x in range(n) :
#         yield x % 2 
        
# evens = myGenerator2(9000000)
 
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))

# print("\n")


# def myGenerator3(n) :
#     for x in range(n) :
#         yield x % 2  
        
# odds = myGenerator3(9000000)
 
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))



# def myGenerator(n) :
#     for x in range(n) :
#         yield x ** 3
        
# values = myGenerator(9000000)
 
# # print(next(values))
# # print(next(values))
# # print(next(values))
# # print(next(values))
# # print(next(values))


# for i in range(1 ,10) :
#     print(next(values), end=" ")

# def myGenerator2(n) :
#     for x in range(n) :
#         yield x % 5
        
# values2 = myGenerator2(9000000)
 
# print(next(values2))
# print(next(values2))
# print(next(values2))
# print(next(values2))
# print(next(values2))


def myGenerator(n) :
    for x in range(n) :
        yield x * 2
        
values = myGenerator(9000000)


for i in range(1 , 100) :
    print(next(values), end=" ")