import asyncio
import time
def heavy_cpu_function():
    sum=0
    
    start_time=time.perf_counter()
    for i in range(100_000_000):
        sum+=i
        
    print(sum)
    end_time=time.perf_counter()
    print(f"end time {end_time-start_time} ")

async def task(task_id: int):
    print(f"Async Task {task_id}: Start")
    await asyncio.sleep(1)
    print(f"Async Task {task_id}: Finish")


async def main():
    start_time=time.perf_counter()

    tasks=[asyncio.create_task(task(i))for i in range (1,4)]
    
    await asyncio.sleep(0.1)

    heavy_cpu_function()

    await asyncio.gather(*tasks)

    end_time=time.perf_counter()


if __name__ == "__main__":
    asyncio.run(main())
