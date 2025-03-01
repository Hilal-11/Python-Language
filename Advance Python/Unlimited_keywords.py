
# def add_student_details(**kwargs) :
#     for i in kwargs :
#         print(i)
    
# add_student_details(name="Hilal", age=22, rollno=101)


# def add_student_details(**kwargs) :
#     for i in kwargs :
#         print(kwargs)
    
# add_student_details(name="Hilal", age=22, rollno=101)

 

# def add_student_details(**kwargs) :
#     for i in kwargs :
#         print(kwargs[i])
    
# add_student_details(name="Hilal", age=22, rollno=101)


def add_student_details(**kwargs) :
    for i , j in kwargs.items() :
        print(f"{i} = {j}")
    
add_student_details(name="Hilal", age=22, rollno=101)