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



class Dog:
    def __init__(self , name , breed , owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def bark(self , name) :
        print(f"{self.name} is barking")
        
class Owner :
    def __init__(self , name , address , contect_no):
        self.name = name
        self.address = address
        self.contect = contect_no
        

owner1 = Owner("Joe" , "657-Tokyo" , "777-000-666")
dog1 = Dog("Tommy" , "Male-dog" , owner1)
    
print(dog1.owner.contect)
        
        


# another example

# class User :
#     def __init__(self , username , email , password):
#         self.username = username
#         self.email = email
#         self.password = password
    
#     def greeting(self) :
#         print(f"hi {self.username} how are you...")
        

# user1 = User("Rio" , "xyz123@gmail.com" , "01010011")
# user1.greeting()



# private and protected

# class User :
#     def __init__(self , username , email , password):
#         self.username = username
#         self._email = email
#         self._password = password
    
#     def greeting(self) :
#         print(f"hi {self.username} how are you...")
        

# user1 = User("Rio" , "xyz123@gmail.com" , "01010011")
# print(user1._email)
# print(user1._password)

# user1._email = "rio123@gmai.com"
# user1._password = "password" 

# print(user1._email)
# print(user1._password)




# getters and setters

# class User :
#     def __init__(self , username , email , password):
#         self.username = username
#         self.__email = email
#         self.__password = password
    
    
#     def get_email(self):
#         return self.__email
    
#     def set_email(self , newEmail) :
#         if "@" in newEmail : 
#             self.__email = newEmail
        
        
#     def greeting(self) :
#         print(f"hi {self.username} how are you...")
        

# user1 = User("Rio" , "xyz123@gmail.com" , "01010011")
# print(user1.get_email())
# user1.set_email("hilal123@gmail.com")
# print(user1.get_email())


# __str__()

# class User :
#     def __init__(self , username , email , password):
#         self.username = username
#         self.email = email
#         self.password = password
        
#     def __str__(self):
#         return f"username is {self.username} and email is {self.email}"
        
        
# user1 = User("Hilal" , "hilalahmadcodedev123@gmail.com" , "10100011")
# print(user1)



# static attributes

# class User :
#     user_count = 0
    
#     def __init__(self , username , email):
#         self.username = username
#         self.email = email
#         User.user_count += 1
        


# user1 = User("Abc" , "abc@gmail.com")
# user2 = User("xyz" , "xyz@gmail.com")
# user3 = User("xyz" , "xyz@gmail.com")
# print(User.user_count) 



# static Mathods

   