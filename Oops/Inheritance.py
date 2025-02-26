
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
    
        
        
homosapiens = Human("Earth" , "random" , "6-feet" , "60-above") 
male1 = Male("Fakarchand" , 100 , "yathlampoor" , "PTSD")
female1 = Female("tokyo" , "20" , "phillippens" , "12th-fail")

print(male1.planet)
print(male1.color)
print(male1.height)
print(male1.weight)
print(male1.name)
print(male1.age)
print(male1.address)
print(male1.qualification)

print("\n\n")

print(female1.planet)
print(female1.color)
print(female1.height)
print(female1.weight)
print(female1.name)
print(female1.age)
print(female1.address)
print(female1.qualification)
