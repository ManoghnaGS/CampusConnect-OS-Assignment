
import threading

counter = 0

lock = threading.Lock()

ITERATIONS = 10000


def increment():
    global counter

    for _ in range(ITERATIONS):

        # Critical Section
        with lock:
            temp = counter
            temp += 1
            counter = temp


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("=" * 50)
print("SYNCHRONIZED VERSION")
print("=" * 50)
print("Expected Counter :", ITERATIONS * 2)
print("Actual Counter   :", counter)
