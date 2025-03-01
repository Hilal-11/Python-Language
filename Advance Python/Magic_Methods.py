

# Dunder magic methods

class Person :
    def __init__(self , name , age , address):
        self.name = name
        self.age = age
        self.address = address
        
    def __del__(self) :
        print("object is deconstructed")
    
p = Person("Rio" , 22 , "India")
# manually deleted 
# del p 

        
class Vector :
    def __init__(self , x , y):
        self.x = x
        self.y = y
    # operating overloading
    def __add__(self , other) :
        return Vector(self.x + other.x , self.y + other.y)

    def __repr__(self):
        return f"X : {self.x} , Y : {self.y}"
    
    def __len__(self):
        return 10
    
    def __call__(self) :
        print("Hello i was called")




v1 = Vector(10 , 20)
v2 = Vector(4 , 6)
v3 = v1 + v2

print(v3)
v3() # call
print(v3.x)
print(v3.y)
print(len(v3))
