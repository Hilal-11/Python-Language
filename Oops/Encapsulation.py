


#   Global Data members and member functions

# class Car :
#     def __init__(self , name , brand):
#         self.name = name
#         self.brand = brand
        
#     def show_car_info(self) :
#         print(f"Car is {self.name} and brand is {self.brand}")

        
# car1 = Car("Swift" , 2020)
# car1.show_car_info()


# privete data manbers and data functions

class Car :
    def __init__(self , name , model , millage , licience):
        self.name = name
        self.model = model
        self._millage = millage # protected
        self._licience = licience    # protected
        
    def car_info(self) :
        print(f"car is {self.name}, model {self.model}, millage {self._millage} and licience {self._licience}")
        
    
car1  = Car("Audi" , 2022 , "89kms" , False)
car1.car_info()

# try to manipulate 
car1.name = "BMW"
car1.model = "2025"
car1.millage = "90kms" # not updated because the (protected) if we want to update/manipulate we must use backslash (_)
car1.licience = True # not updated because the (protected) if we want to update/manipulate we must use backslash (_)

car1.car_info()