


#   Global Data members and member functions

# class Car :
#     def __init__(self , name , brand):
#         self.name = name
#         self.brand = brand
        
#     def show_car_info(self) :
#         print(f"Car is {self.name} and brand is {self.brand}")

        
# car1 = Car("Swift" , 2020)
# car1.show_car_info()


# protected data manbers and data functions

# class Car :
#     def __init__(self , name , model , millage , licience):
#         self.name = name
#         self.model = model
#         self._millage = millage # protected
#         self._licience = licience    # protected
        
#     def car_info(self) :
#         print(f"car is {self.name}, model {self.model}, millage {self._millage} and licience {self._licience}")
        
    
# car1  = Car("Audi" , 2022 , "89kms" , False)
# car1.car_info()

# # try to manipulate 
# car1.name = "BMW"
# car1.model = "2025"
# car1.millage = "90kms" # not updated because the (protected) if we want to update/manipulate we must use backslash (_)
# car1.licience = True # not updated because the (protected) if we want to update/manipulate we must use backslash (_)

# car1.car_info()


# privete data manbers and data functions

class Students: 
    def __init__(self , name , address , course , collage , contect , email , password , courseCode , regestration_no):
            self.name = name
            self.address = address
            self.course = course
            self.collage = collage
            self.__contect = contect
            self.__email = email
            self.__password = password
            self.__courseCode = courseCode
            self.__regestration_no = regestration_no
            
    def studentInfo(self) :
        print(f'''
            name : {self.name}
            address : {self.address}
            course : {self.course}
            collage : {self.collage}
            ''')
    def student_personal_info(self):
        print(f'''
            contect : {self.__contect}
            email: {self.__email}
            password :{self.__password}
            course code: {self.__courseCode}
            regestration: {self.__regestration_no} 
            ''')
    def set_student_personal_info(self , contect , email , password , coursecode , regNo):
        self.__contect = contect
        self.__email = email
        self.__password = password
        self.__courseCode = coursecode
        self.__regestration_no = regNo
        
        

student1  = Students("Hilal", "lolab" , "BCA" , "GDC-Fakarchand" , "772-282-828" , "hilalahmadcodedev123@gmail.com" , "01010011" , "bca_fakarchand0101" , "001101063")
student1.studentInfo()
student1.student_personal_info()

# manipulation privete data using getters and setters
student1.set_student_personal_info("990-883-000" , "abc123@gmail.com" , "01010101" , "gdgdghka" , "01083764")
student1.student_personal_info()