from concurrent.futures import ThreadPoolExecutor
import threading
import time

shared_mem=0
Lock=threading.Lock()

def modifyingSharedmem_Withoutlock(_):
    global shared_mem
    for _ in range(1000):
        temp=shared_mem
        time.sleep(0)
        shared_mem=temp+1

def modifyingSharedmem_Withlock(_):
        global shared_mem
        for _ in range(1000): 
            with Lock:
                temp=shared_mem
                time.sleep(0)
                shared_mem=temp+1
    
def main():
    global shared_mem
    executor=ThreadPoolExecutor(max_workers=10)
    shared_mem=0
    list(executor.map(modifyingSharedmem_Withoutlock,range(10)))
    print(f"expected 10000 : {shared_mem}")
    shared_mem=0
    list(executor.map(modifyingSharedmem_Withlock,range(10)))
    print(f"expected 10000 : {shared_mem}")

if __name__=="__main__":
    main()