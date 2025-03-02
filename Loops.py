# print the series of even and odds from 1 to 100

# n = 100
# print("Even Numbers = ")
# for i in range(n) :
#     if i % 2 == 0 :
#         print(i, end=" ")
        
# print("\n")        
# print("Odd Numbers = ")
# for i in range(n): 
#     if i % 2 != 0:
#         print(i , end=" ")
        
# using functions

def evenSeries(n) :
    for i in range(n) :
        if n % 2 == 0:
            print(i,end=" ")

def oddSeries(n) :
    for i in range(n) :
        if n % 2 != 0: 
            print(i,end="")
            
            
evenSeries(200)
print("\n")
oddSeries(200)


print("\n \n")

# nested loops

for i in range(5) :
    for j in range(i):
        print("*" , end=" ")
    print("\n")
    
    
greeting = "Hello python"