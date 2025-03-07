
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