
class Human :
    def __init__(self , planet, color , height , weight):
        self.planet = planet
        self.color = color
        self.heigh = height
        self.weight = weight
    
class Male(Human):
    def __init__(self , name , age , address , qualification):
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification
        
    
class Female(Human) :
    def __init__(self , name , age , address , qualification):
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification
    
        
        
male1 = Male("Fakarchand" , 100 , "yathlampoor" , "PTSD")
male1.planet = "Earth"
male1.color = "rabdom"
male1.height = "6-feet"
male1.weight = "60-above"


print(male1.planet)
print(male1.color)
print(male1.height)
print(male1.weight)
print(male1.name)
print(male1.age)
print(male1.address)
print(male1.qualification)

print("\n")
female1 = Female("tokyo" , "20" , "phillippens" , "12th-fail")
female1.planet = "Earth"
female1.color = "rabdom"
female1.height = "6-feet"
female1.weight = "60-above"

print(female1.planet)
print(female1.color)
print(female1.height)
print(female1.weight)
print(female1.name)
print(female1.age)
print(female1.address)
print(female1.qualification)



# Inheritance Types
    # single inheritance
    # multi-level inheritance
    # multiple inheritance
    # Hierarchial Inheritance
    # hibrid inheritance


# single inheritance

class Animal :
    def __init__(self , name , catagory):
        self.name = name
        self.catagory = catagory
    def speak(self) :
        return "animals mske sound"
        

class Dog(Animal) :
    def __init__(self , color):
        self.color = color
    def speak (self) :
        return "bark"


dog1 = Dog("black")
dog1.name = "Tommy"
dog1.catagory = "pitbul"

print(f'''
        name: {dog1.name}
        catagory: {dog1.catagory}
        color: {dog1.color}
      ''')       
    














    