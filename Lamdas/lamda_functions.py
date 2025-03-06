
# Lamda functions in python 

# lambda arguments : expression
    # a lamda function is a small anonomous function , that takes number of argumants and have only 
    # single/one expression
# lambda x , y : x + y

add = lambda x , y : x + y
print(add(10 , 20))

mul = lambda x , y , z : x*y*z
print(mul(10 , 6 , 2))


# sum = lambda **args : 

# students = [("Hilal" , 90), ("waseem" , 89) , ("Aadil", 80)]
# print(students)
# for iter in students :
#         for i in iter :
#             print(i)
            

students = [("Hilal" , 60), ("waseem" , 89) , ("Aadil", 70)]
# students.sort()
# print(students)

def sort_students(data) :
    return data[1]

students.sort(key=sort_students)
print(students)

students.sort(key=sort_students , reverse=True)
print(students)