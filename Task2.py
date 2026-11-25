import time
import asyncio
async def task2():
    start_time=time.perf_counter()

    for i in range (0,8):
        print(f"task{i} started")
        await asyncio.sleep(1)
        print(f"task{i} ended")

    print(time.perf_counter()-start_time)


def main():
    asyncio.run(task2())

if __name__ == "__main__":
    main()