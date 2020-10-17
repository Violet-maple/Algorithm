# coding: utf-8

import asyncio


async def display(num):
    await asyncio.sleep(1)
    print(num)


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.wait(
        [display(num) for num in range(10)]
    )
)
loop.close()
