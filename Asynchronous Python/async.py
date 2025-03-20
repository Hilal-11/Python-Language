import asyncio

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

async def function1() :
    task = asyncio.create_task(function2())
    print("one")
    await asyncio.sleep(1)
    print("four")
    await asyncio.sleep(1)
    print("five")

async def function2() :
    print("Two")
    await asyncio.sleep(1)
    print("three")
    
asyncio.run(function1())