import asyncio


async def fun_1():
    print(1)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到lst中的其他任务
    print(2)


async def fun_2():
    print(3)
    await asyncio.sleep(2)
    print(4)


lst = [
    asyncio.ensure_future(fun_1()),
    asyncio.ensure_future(fun_2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(lst))
