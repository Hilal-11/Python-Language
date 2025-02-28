
# random module

import random

print(random.random()) # generates the number between 0 - 1     # Example output: 0.675484539

# generate random between some range (from - to)

ran = random.uniform(10 , 20) # random generated between n - m
print(ran)

print(random.randint(1 , 100))    # Example output: 42

# random.randrange(start, stop, step)

print(random.randrange(1 , 100 , 10))


fruits = ["apple", "banana", "cherry", "mango"]
print(random.choice(fruits))


data = ['A' , 'B' , 'C' , 'D' , 'E' , ' F']
randomIdx = random.randint(0 , len(data))
print(data[randomIdx])