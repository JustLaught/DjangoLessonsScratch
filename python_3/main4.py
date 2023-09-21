import time
import concurrent.futures
import threading


class DataBase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print(f"Thread {name} started update")
        # self._lock.acquire()
        with self._lock:
            value = self.value
            value += 1
            time.sleep(0.1)
            self.value = value
        # self._lock.release()
        print(f"Thread {name} finished update")

if __name__ == "__main__":
    db = DataBase()
    print(f"Test update value is {db.value}")
    with concurrent.futures.ThreadPoolExecutor() as exe:
        exe.map(db.update, range(1, 3))
    print(f"End test value now {db.value}")
