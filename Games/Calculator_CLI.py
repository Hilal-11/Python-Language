
def perform_addition(x , y) :
    result = x + y
    print(f"Addition of {x} + {y} = " , result)

def perform_subtraction(x , y):
    result = x - y
    print(f"Subtraction of {x} - {y} = " , result)
    
def perform_multiplication(x , y):
    result = x * y
    print(f"Multiplication of {x} * {y} = " , result)
def perform_division(x , y):
    result = x / y
    print(f"Division of {x} / {y} = " , result)
    
def perform_comparision(x , y):
    if(x > y):
        print(f"{x} is greaterthan {y}")
    elif(x < y):
        print(f"{x} is lessthan {y}")
    else:
        print(f"{x} is equal to {y}")
        
def main() :
    while True:
        print("\n Python CLI Calculator  | Choose an option to perforn calculations \n")
        print("*" * 100)
        print("1:- Addition operation")
        print("2:- Subtraction operation")
        print("3:- Multiplication operation")
        print("4:- Division operation")
        print("5:- Comparision operation")
        print("6:- Exit")
        
        print("*" * 100)
        
        choice = input("Enter your choice :- ")  
        
        if(choice == '1') :
            num1 = int(input("Enter first number :- "))
            num2 = int(input("Enter second number :- "))
            perform_addition(num1 , num2)
        elif(choice == '2'):
            num1 = int(input("Enter first number :- "))
            num2 = int(input("Enter second number :- "))
            perform_subtraction(num1 , num2)
        elif(choice == '3'): 
            num1 = int(input("Enter first number :- "))
            num2 = int(input("Enter second number :- "))
            perform_multiplication(num1 , num2)
        elif(choice == '4') :
            num1 = int(input("Enter first number :- "))
            num2 = int(input("Enter second number :- "))
            if(num2 == 0):
                print("Dividing by zero is not allowed")
            else:
                perform_division(num1 , num2)
        elif(choice == '5') :
            num1 = int(input("Enter first number :- "))
            num2 = int(input("Enter second number :- "))
            perform_comparision(num1 , num2)
        elif(choice == '6') :
            return
        else: 
            print("Invalid choice selected")
            break
            
                  
    
if __name__ == '__main__' :
    main()