
def perform_addition(x , y) :
    result = x + y
    print(f"Addition of {x} + {y} = " , result)

def perform_subtraction(x , y):
    result = x - y
    print(f"Subtraction of {x} - {y} = " , result)
def main() :
    
    while True:
        
        print("\n Python CLI Calculator  | Choose an option to perforn calculations \n")
        print("1:- Addition operation")
        print("2:- Subtraction operation")
        print("3:- Multiplication operation")
        print("4:- Division operation")
        print("5:- Comparision operation")
        
        choice = input("Enter your choice :- ")  
        
        if(choice == '1') :
            num1 = int(input("Enter first number :- "))
            num2 = int(input("Enter second number :- "))
            perform_addition(num1 , num2)
        if(choice == '2'):
            num1 = int(input("Enter first number :- "))
            num2 = int(input("Enter second number :- "))
            perform_subtraction(num1 , num2)
            
                  
        

if __name__ == '__main__' :
    main()