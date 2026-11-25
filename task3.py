import time 
import asyncio

async def task(id:int):
    print(f"task {id} started")
    await asyncio.sleep(1)
    print(f"task {id} ended")

async def main():
    start_time=time.perf_counter()
    tasks=[]
    for i in range(0,8):
        tasks.append(task(i))
    await asyncio.gather(*tasks)

    total_Time=time.perf_counter()-start_time

    print(total_Time)

if __name__ == "__main__":
    asyncio.run(main())

    