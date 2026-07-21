
import threading

counter = 0
barrier = threading.Barrier(2)

ITERATIONS = 10000


def increment():
    global counter

    for _ in range(ITERATIONS):

        # Read
        temp = counter

        # Force both threads to read the same value
        barrier.wait()

        # Modify
        temp += 1

        # Write
        counter = temp


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("=" * 50)
print("UNSYNCHRONIZED VERSION")
print("=" * 50)
print("Expected Counter :", ITERATIONS * 2)
print("Actual Counter   :", counter)
