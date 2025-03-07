print("File Handling in python")


# # f = open("demofile.txt")
# try: 
#     f = open("demofile.txt", "r") 
#     print(f.read())
# except FileNotFoundError :
#     print("the file 'demofile.txt' does not exist")


# try :
#     with open("demofile.txt" , "r") as f:
#         print(f.read())
# except FileNotFoundError :
#     print("the file 'demofile.txt' does not exists")



# create the file and write some content on it and open to read
with open("demo.txt" , "w") as f:
    f.write("Hello! Welcome to demofile.txt This file is for testing purposes. Good Luck!")
# now open this file
try :
    with open("demo.txt" , "r") as f:
        print(f.read())
except FileNotFoundError:
    print("The file 'demo.txt' does't exists")
    
    
print("\n\n")
try :
    with open("demofile.txt" , "r") as f:
        print(f.read()) 
except FileNotFoundError :
    print("The file 'demofile.txt' does't exists")