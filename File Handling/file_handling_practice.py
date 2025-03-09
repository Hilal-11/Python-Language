import os

# create a file write some content on it and read

with open("hilal.txt" , "w") as f:
    f.write("Hello hilal wel come...")
try:
    with open("hilal.txt" , "r") as f:
        print(f.read())

except FileNotFoundError :
    print("file does't not exists")
    
# appending on this file
with open("hilal.txt" , 'a') as f:
    f.write(" this is hilal ....")
    
try :
    with open("hilal.txt" , 'r') as f :
        print(f.read())
except FileNotFoundError :
    print("File does't exist")
    
if os.path.exists("hilal.txt"):
    os.remove("hilal.txt")
else :
    print("file does't exists in system, please give the correct path")
    
    