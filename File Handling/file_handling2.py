
# create a file and write some content
with open("javascript.js" , "w") as f:
    f.write("console.log('hello javascript and typescript')")
# open file in try-exception block and print the content on it
try :
    with open("javascript.js" , "r") as f:
        print(f.read())
except FileNotFoundError :
    print("the file 'javsccript.js' does't exists")
    
# manipulation on existing file
with open("javascript.js" , "w") as f:
    f.write("document.write('hello javascript and typescript')")
# print again to see the modifications
try :
    with open("javascript.js" , "r") as f:
        print(f.read())
except FileNotFoundError :
    print("the file 'javsccript.js' does't exists")
    
    
print("\n\n")
    
fl = open("typescript.ts" , "w")
fl.write("console.log('Typescript is advance version of javascript') document.write('developed by microsoft research foundation')")
# fl.close()
try :
    fl = open("typescript.ts" , "r")
    print(fl.read())
    # fl.close()
except FileNotFoundError :
    print("The file 'typescript.ts' does't exists")
    
    
    
    
    
    
    
    