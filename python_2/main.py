# import threading
import concurrent.futures
# import asyncio
# import multiprocessing
import time

start = time.time()

def do_something(sec):
    print(f"sleep {sec} sec")
    time.sleep(sec)
    return f"done sleeping {sec} seconds"

with concurrent.futures.ThreadPoolExecutor() as exec:
    sec = [5, 4, 3, 2, 1]
    # res = [exec.submit(do_something, 2) for _ in range(10)]
    res = exec.map(do_something, sec) 

for resl in res:
    print(resl)

# for f in concurrent.futures.as_completed(res):
#     print(f.result())

# with concurrent.futures.ThreadPoolExecutor() as exec:
#     f1 = exec.submit(do_something, 1)
#     f2 = exec.submit(do_something, 2)

# print(f1.result())
# print(f2.result())
# threads = []
# seconds = [5, 4, 3, 2, 1]

# for sec in seconds:
#     f = threading.Thread(target=do_something, args=[sec])
#     f.start()
#     threads.append(f)
    
# for threds in threads:
#     threds.join()

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()
# t1.join()
# t2.join()


finish = time.time()

print(f"Finished in {finish-start} seconds")