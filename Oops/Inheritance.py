
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
    
    
# multi-level inheritance


# multiple inheritance

class Father :
    def __init__(self , name , age):
        self.name = name
        self.age = age
class Mother :
    def __init__(self , height , weight):
        self.height = height
        self.weight = weight
        
class Child(Father , Mother) :
    def __init__(self , gender):
        self.gender = gender
    def displayChildInfo(self) :
        print(f'''
              name : {self.name}
              age : {self.age}
              height : {self.height}
              weight : {self.weight}
              gender : {self.gender} 
            ''')  


son = Child("male")
son.name = "Danver"
son.age = "12"
son.height = "4-feet"
son.weight = "28-kg"

son.displayChildInfo()
print("\n")

daughter = Child("female")
daughter.name = "Tokiyo"
daughter.age = "15"
daughter.height = "4.6-feet"
daughter.weight = "34-kg"

daughter.displayChildInfo()


#  inheritance examples

class Vehicles :
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self) :
        print("Vehicles can start")
    def stop(self) :
        print("Vehicles can stop")
        
class Car(Vehicles):
    def __init__(self,  brand , model , year  , color , number_of_wheels):
        super().__init__(brand , model , year)
        self.color = color
        self.number_of_wheels = number_of_wheels
    
    def displayCarInfo(self) :
        print(f'''
              car name : {self.brand}
              car model : {self.model}
              car brand : {self.brand}
              car year : {self.year}
              car wheels : {self.number_of_wheels}
            ''')
        
class Bike (Vehicles):
    def __init__(self , brand , model  , year , color , number_of_wheels) :
        super().__init__(brand , model , year)
        self.color = color
        self.number_of_wheels = number_of_wheels
    
    def displayBiksInfo(self) :
        print(f'''
            bike name : {self.brand}
            bike model : {self.model}
            bike brand : {self.brand}
            bike year : {self.year}
            bike wheels : {self.number_of_wheels}
        ''')

car1 = Car("Bugati", 2025, "2-year", "gray", 4)
car1.displayCarInfo()
car1.start()
car1.stop()

print("\n")

bike1 = Bike("KTM-200", 2022 , "3-years" , "Orange" , 2)
bike1.displayBiksInfo()
bike1.start()
bike1.stop()



class Human :
    def __init__(self , planet, color , height , weight):
        self.planet = planet
        self.color = color
        self.heigh = height
        self.weight = weight
        
    def eat(self):
        print("Humans can eat")
    def sleep(self):
        print("Humans can sleep")
    def walk(self) :
        print("Humans can walk")
    def talk(self) :
        print("Humans can talk")
    
class Male(Human):
    def __init__(self ,planet, color , height , weight,  name , age , address , qualification):
        super().__init__(planet, color , height , weight)
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification
        
    def displayMaleProperties(self) :
        print(f'''
              planet : {self.planet}
              name: {self.name}
              age : {self.age}
              address: {self.address}
              height: {self.heigh}
              weight: {self.weight}
              color : {self.color}
              qualification : {self.qualification}
            ''')
        
    
class Female(Human) :
    def __init__(self , planet, color , height , weight, name , age , address , qualification):
        super().__init__(planet, color , height , weight,)
        self.name = name
        self.age = age
        self.address = address
        self.qualification = qualification
    
    def displayFemaleProperties(self):
        print(f'''
            planet : {self.planet}
            name: {self.name}
            age : {self.age}
            address: {self.address}
            height: {self.heigh}
            weight: {self.weight}
            color : {self.color}
            qualification : {self.qualification}
        ''')
        
male1 = Male("Earth" , "white" , "6-feet" , "60kg" , "Fakarchand", "20" , "kupwara" , "BCA")
male1.displayMaleProperties()
male1.eat()
male1.sleep()
male1.talk()
male1.walk()
female1 = Female("Earth" , "dark" , "6.5-feet" , "68kg" , "Faizan", "67" , "kupwara kralpoors" , "MCA")
female1.displayFemaleProperties()
female1.eat()
female1.sleep()
female1.talk()
female1.walk()
