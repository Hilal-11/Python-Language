    # classes
# class Dog:
#     def bark(self):
#         print("whoff whoff")
        
    

 # objects
# dog1 = Dog()
# dog2 = Dog()

# dog1.bark()
# dog2.bark()



class Person:
    def __init__(self , name , age , address , gender , profession):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.profession = profession
        
    def displayPersonInfo(self) :
        print(self.name)
        print(self.age)
        print(self.address)
        print(self.gender)
        print(self.profession)
        

person1 = Person("Hilal" , 20 , "Kupwara Lolab" , "Male" , "Computer Scientest")
person2 = Person("Waseem" , 21 , "Kupwara Lolab" , "Male" , "Computer Programmer")

person1.displayPersonInfo()
print("\n")
person2.displayPersonInfo()
        
