import asyncio
import threading
import time

shared_counter = 0
lock = threading.Lock()  


def cpu_work(task_id: int, iterations: int):
    """Regular synchronous function that runs inside a thread."""
    global shared_counter
    print(f"Task {task_id}: Running CPU work in thread {threading.current_thread().name}")

    
    local_sum = 0
    for i in range(iterations):
        local_sum += i

    
    for _ in range(1000):
        with lock:
            temp = shared_counter
            time.sleep(0)  
            shared_counter = temp + 1

    return local_sum


async def async_task(task_id: int):
    """Async task that requests CPU work without blocking the event loop."""
    print(f"Async Task {task_id}: Requesting CPU work...")

    
    result = await asyncio.to_thread(cpu_work, task_id, 5_000_000)

    print(f"Async Task {task_id}: Finished (local_sum={result})")


async def main():
    start_time = time.perf_counter()

    # Launch 5 async tasks concurrently
    tasks = [async_task(i) for i in range(1, 6)]
    await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start_time
    print(f"\nFinal shared_counter (Expected 5000): {shared_counter}")
    print(f"Total time: {elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())