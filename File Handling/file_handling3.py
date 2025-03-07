
# try :
#     with open("typescript.ts" , "r") as f :
#         print(f.read())
# except FileNotFoundError :
#     print("The file 'typescript.ts' does not exist")
    
    
#   Appending content on existing file

with open("typescript.ts" , "a") as f:
    f.write("const x = 10 \n console.log(x)")
    f.close()
try :
    with open("typescript.ts" , "r") as f:
        print(f.read())
        f.close()
except :
    print("the file 'typescript.ts' does't exists")