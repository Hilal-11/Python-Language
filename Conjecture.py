

# mathematical problem Colartz conjecture

n = int(input("Enter value of n for colartz conjectue :- "))
counter = 0
while n != 1:
    if n % 2 != 0:
        print(n , "\t",end=" ")
        n = (3 * n) + 1
        counter = counter + 1
    else :
        print(n , "\t", end="")
        n = (n / 2)
        counter = counter + 1
    
print(f"\n \n total number of steps to reach 1 for value {n} = {counter}")