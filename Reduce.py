from functools import reduce

# reduce function in python


data = [1, 2, 3, 4, 5]
def sum_of_list(x, y) :
    return x + y
sum_list = reduce(sum_of_list , data)
print(sum_list)

# lamdas
sum = reduce(lambda x , y : x + y , data)
print(sum)

# find maximum element 
elements = [9 , 4 , 5 , 2 , 7 , 29]
def maximum(x , y) :
    return max(x , y)
maxElm = reduce(maximum , elements)
print(maxElm)
# find minimum element
def minimum(x , y) :
    return min(x , y)
minElm = reduce(minimum , elements)
print(minElm)