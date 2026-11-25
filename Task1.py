import time
def run_sync_tasks():
    start_time= time.perf_counter()
    i=0
    
    for i in range(1,9):
        print(f"task {i} started")
        time.sleep(1)
        print(f"task {i} ended")

    end_time=time.perf_counter()
    total_time=end_time-start_time
    print(total_time)
        
def main():
    run_sync_tasks()
    
if __name__ == "__main__":
    main()
