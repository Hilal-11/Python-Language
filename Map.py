
# map function of python

data = [10 , 20 , 30 , 40]
print(data)
result = map(str , data) 
print(list(result))
    

print("\n")
# example 2
l = [2 ,4 ,6 ,8,10]

def double(val) :
    return val * 2

result = list(map(double , l))
print(result)