
# def generateList(n) :
#     items = []
#     for x in range(n) :
#         items.append(x)
#     return items

# listItems = generateList(100)
# print(listItems)



def list_n(n) :
    num = 0
    numsList = []
    while num < n:
        numsList.append(num)
        num += 1
    return numsList
myList = list_n(200)
print(myList)


# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
 
sum_of_first_n = firstn(1000000)
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))
print(next(sum_of_first_n))



print("\n")
# doubles = [2 * i for i in range(100)]
# print(doubles)

doubles = list(2 * i for i in range(100))
print(doubles)