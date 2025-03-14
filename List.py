

# lists in python

fruits = ["apple" , "Mango" , "Orange" , "Banana" , "Grapes", "Watermelon" , "Pineapple" , "Papaya"]
print(fruits)

# appending new element to the list
fruits.append("Pineapple")
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# nagative indexing
print("\n \n")

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])



print("\n")

# Slicing

print(fruits[0: 4])
print(fruits[0: 6])

print(fruits[::2])


# adding element in list
# adding element in list


data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(data)

data[0] = 105
print(data)


data.append(110)
print(data)


data.insert(1 , 15);
print(data)

data2 = [200, 300, 400, 500, 600]

data.extend(data2)
print(data)


# removing element from list


print("\n")
# remove items in list
     # remove() method
     # pop() method
     # del keyword
     # clear() method
# friends = ["Hilal" , "Waseem" , "Junaid" , "Aamir" , "Shahid" , "Nadeem" , "Rizwan" , "Nasir"]
# print(friends)

# friends.remove("Hilal")
# print(friends)

# friends.pop(0)
# print(friends)

# del friends[0]
# print(friends)

# friends.clear()
# print(friends)


# iteration (loops)
friends = ["Hilal" , "Waseem" , "Junaid" , "Aamir" , "Shahid" , "Nadeem" , "Rizwan" , "Nasir"]
for friend in friends: 
    print(friend)

print("\n")
# while loop

i = 0
while i < len(friends):
    print("index[",i,"]",friends[i])
    i += 1


print("\n")
print("\n")

list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]
     
print(list[0][0],end=" ")
print(list[0][1],end=" ")
print(list[0][2],end=" ")
print(list[0][3],end=" ")
print(list[0][4])




#  again lists

# list is a data structure 
# list allows diplication
# list is Mutable
# list is ordered
# allows to store multiiple values is a single variable
# items = [11 , 9 , 2 , 6 , 10]
# items[0] = 100
# items[len(items) -1] = 99
# print(items)

items = [10 , 22 , 34 , 90 , 'A' , 'X']
print(items)

# get length of list 
length = len(list)
print(length)

#  slicing() --> extrating the portion of list

# print(slice(list[0 : 3]))

items.append('Hilal')
print(items)

items.pop()
print(items)

items.insert(0 , "Waseem")
print(items)
print("\n\n")



dataItems = [ 18 ,10 , 12 , 14 , 16]
print(dataItems)

# dataItems.sort()
# print(dataItems)

# idx = dataItems.index(12)
# print(idx)

# dataItems.clear()
# print(dataItems)

# dataItems.reverse()
# print(dataItems)



print("\n\n")