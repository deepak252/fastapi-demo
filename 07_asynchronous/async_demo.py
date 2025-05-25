import asyncio
import time

"""
asyncio is a Python library to write concurrent code using the async/await syntax.
It provides a way to run multiple tasks asynchronously.
It uses an event loop to manage and schedule asynchronous tasks.
Ideal for I/O-bound and high-level structured network code.

"""

# # async is a keyword used to define coroutines
# async def counter():     # coroutine function.
#     print("One")
#     await asyncio.sleep(1) # await keyword used to pause the coroutine until the awaited thing is done.
#     print("Two")

# CPU Intensive Task
async def counter():
    for i in range(30000000):
        pass

async def main():
    # asyncio.gather() is similar to Promise.all() in js
    await asyncio.gather(counter(), counter(), counter())

if __name__ == "__main__":
    start_time = time.time()

    asyncio.run(main())

    end_time = time.time()

    print(f"Async Execution Time: {end_time-start_time} seconds")
    # Async Execution Time: 1.9255468845367432 seconds