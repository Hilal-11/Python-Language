


#   Global Data members and member functions

class Car :
    def __init__(self , name , brand):
        self.name = name
        self.brand = brand
        
    def show_car_info(self) :
        print(f"Car is {self.name} and brand is {self.brand}")

        
car1 = Car("Swift" , 2020)
car1.show_car_info()