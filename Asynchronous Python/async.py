import asyncio
import time
# async def greeting() :
#     print("execution start")
#     await asyncio.sleep(2)
#     print("Asynchronous execution is not a multi-threading or multi-tasking , it is non-blocking code")
#     await asyncio.sleep(3)
#     print("execution end")
#     await asyncio.sleep(1)
#     print('Hello')
    


# # asyncio.run(greeting()) 
# asyncio.run(greeting())


# async def function1() :
#     print("one")
#     await asyncio.sleep(1)
#     print("two")
#     await asyncio.sleep(1)
#     await function2()
#     await asyncio.sleep(1)
#     print("five")
    
    
# async def function2() :
#     print("three")
#     await asyncio.sleep(1)
#     print("four")
    
    
# asyncio.run(function1())

# async def function1() :
#     task = asyncio.create_task(function2())
#     print("one")
#     await asyncio.sleep(1)
#     print("four")
#     await asyncio.sleep(1)
#     print("five")

# async def function2() :
#     print("Two")
#     await asyncio.sleep(1)
#     print("three")
    
# asyncio.run(function1())



# synchronous manner execution
# def function1() :
#     time.sleep(2)
#     print("Function 1 is executed")

# def function2() :
#     time.sleep(1)
#     print("Function 2 is executed")

# def function3() :
#     time.sleep(3)
#     print("Function 3 is executed")
    
# function1()
# function2()
# function3()

# important !!!
# async def function1() :
#     await asyncio.sleep(1)
#     print("Function 1 is executed")

# async def function2() :
#     await asyncio.sleep(1)
#     print("Function 2 is executed")

# async def function3() :
#     await asyncio.sleep(4)
#     print("Function 3 is executed")
    
# async def main() : 
#     task = asyncio.create_task(function1())
#     await function2()
#     await function3()
    
# asyncio.run(main())



async def function1() :
    await asyncio.sleep(3)
    print("Function 1 is executed")
    return "Hilal"

async def function2() :
    await asyncio.sleep(1)
    print("Function 2 is executed")
    return "Hilal"

async def function3() :
    await asyncio.sleep(2)
    print("Function 3 is executed")
    return "Hilal"
    
async def main() : 
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
    

asyncio.run(main())