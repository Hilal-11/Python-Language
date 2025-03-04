
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


# example first of map function

elements = ["Apple" , "Banana" , "Orange" , "Grapes"]
print(elements)

def concate_with_fruit(elements) :
    return "Fruit "+ elements
result = list(map(concate_with_fruit , elements))
print(result)

print("\n")
print("\n")

# example second of map function
    # conseder the list of integers return only even elements from that list using map()
elms1 = [2, 5 , 7 , 9 , 8 , 3 , 4 , 12 , 16]
def evenElements(elements) :
    if(elements % 2 == 0):
        return elements
    else:
        return 'odd'
evenList = list(map(evenElements , elms1))
print(evenList)
    # conseder the list of integers return only odd elements from that list using map()
elms2= [2, 5 , 7 , 9 , 8 , 3 , 4 , 12 , 16]
def oddElements(elements) :
    if (elements % 2 != 0):
        return elements
    else :
        return 'even'
oddList = list(map(oddElements , elms2))
print(oddList)




# elms1 = [2, 5 , 7 , 9 , 8 , 3 , 4 , 12 , 16]
# def evenElements(elements) :
#     lst = []
#     if(elements % 2 == 0):
#         lst.append(elements)
#     return lst    
# evenList = list(map(evenElements , elms1))
# print(evenList)
#     # conseder the list of integers return only odd elements from that list using map()
# elms2= [2, 5 , 7 , 9 , 8 , 3 , 4 , 12 , 16]
# def oddElements(elements) :
#     if (elements % 2 != 0):
#         return elements
# oddList = list(map(oddElements , elms2))
# print(oddList)




    # this recomeded only with filter function
    # this recomeded only with filter function
    
# elms1 = [2, 5 , 7 , 9 , 8 , 3 , 4 , 12 , 16]

# evenList = list(filter(lambda elms1 : elms1 % 2 == 0 , elms1))
# print(evenList)
#     # conseder the list of integers return only odd elements from that list using map()
# elms2= [2, 5 , 7 , 9 , 8 , 3 , 4 , 12 , 16]

# oddList = list(filter(lambda elms2: elms2 % 2 != 0 , elms2))
# print(oddList)



# names = ["hilal" , "waseem" , "junaid" , "abass" , "aadil"]
# print(names)
# def getUppercase(names):
#     return names.upper()
# names_res = list(map(getUppercase , names))
# print(names_res)

names = ["hilal" , "waseem" , "junaid" , "abass" , "aadil"]
print(names)

names_res = list(map(lambda names: names + " Ahmad" , names))
print(names_res)