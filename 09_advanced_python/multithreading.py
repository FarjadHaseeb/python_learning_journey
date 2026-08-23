import threading
import time

def task(name):
    for i in range(3):
        print(name, i)
        time.sleep(0.5)

threads = [threading.Thread(target=task, args=(f"Task-{i}",)) for i in range(3)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All tasks completed")
