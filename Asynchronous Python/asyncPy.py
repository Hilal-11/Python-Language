import asyncio
import requests

URL = "https://instagram.com/favicon.ico"


async def function1() :
    response = requests.get(URL)
    open("instagram1.ico" , "wb").write(response.content)
    
async def function2() :
    response = requests.get(URL)
    open("instagram2.ico" , "wb").write(response.content)
    
async def function3() :
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
    
    
async def main() :
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
    
asyncio.run(main())