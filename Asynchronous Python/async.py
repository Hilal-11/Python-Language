import asyncio

async def greeting() :
    print("execution start")
    await asyncio.sleep(2)
    print("Asynchronous execution is not a multi-threading or multi-tasking , it is non-blocking code")
    await asyncio.sleep(3)
    print("execution end")
    await asyncio.sleep(1)
    print('Hello')
    


# asyncio.run(greeting()) 
asyncio.run(greeting())