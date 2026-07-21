class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.remaining = burst
        self.wait_time = 0


# -------------------------
# Process Dataset
# -------------------------
processes = [
    Process("P1", 0, 5, 1),   # Low priority (starving process)
    Process("P2", 0, 2, 5),
    Process("P3", 2, 2, 5),
    Process("P4", 4, 2, 5),
    Process("P5", 6, 2, 5)
]

AGING_INTERVAL = 2

time = 0
completed = 0

print("=" * 65)
print("Priority Scheduling with Aging")
print("=" * 65)

print("{:<5}{:<8}{:<10}{:<10}".format(
    "Time", "Process", "Priority", "Waiting"))

while completed < len(processes):

    ready = []

    for p in processes:
        if p.arrival <= time and p.remaining > 0:
            ready.append(p)

    if not ready:
        time += 1
        continue

    # Higher priority number runs first
    ready.sort(key=lambda x: (-x.priority, x.arrival))

    current = ready[0]

    print("{:<5}{:<8}{:<10}{:<10}".format(
        time,
        current.pid,
        current.priority,
        current.wait_time
    ))

    current.remaining -= 1

    if current.remaining == 0:
        completed += 1

    time += 1

    # Aging
    for p in processes:

        if p != current and p.remaining > 0 and p.arrival <= time:

            p.wait_time += 1

            if p.wait_time % AGING_INTERVAL == 0:
                p.priority += 1

print("\nSimulation Finished")
