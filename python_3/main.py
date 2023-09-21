import time
import multiprocessing
import concurrent.futures

start = time.time()

def do_something(sec):
    print(f"Sleep {sec} sec")
    time.sleep(sec)
    return f"Done sleeping {sec} sec"

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as proc:
        processec = proc.map(do_something, range(10, 0, -1))
        for result in processec:
            print(result)

        # procecces = [proc.submit(do_something, 2) for _ in range(16)]
        # for res in concurrent.futures.as_completed(procecces):
        #     print("Result:",res.result())

        # p1 = proc.submit(do_something, 2)
        # p2 = proc.submit(do_something, 1)
        # print(p1.result())
        # print(p2.result())

    # proces = []
    
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     # p.join()
    #     proces.append(p)

    # for pro in proces:
    #     pro.join()

    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # do_something()
    # do_something()

    finish = time.time()

    print(f"Done in {round(finish-start, 2)} sec")