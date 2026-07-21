import csv
from collections import deque

# ------------------------------
# Read Process Data
# ------------------------------
def load_processes(filename):
    processes = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            processes.append({
                "id": row["Process"],
                "arrival": int(row["Arrival"]),
                "burst": int(row["Burst"])
            })

    return processes


# ------------------------------
# Print Results
# ------------------------------
def print_results(name, results):

    print("\n===================================")
    print(name)
    print("===================================")

    total_wait = 0
    total_turn = 0

    print("{:<8}{:<10}{:<10}".format(
        "Process", "Waiting", "Turnaround"))

    for p in results:

        print("{:<8}{:<10}{:<10}".format(
            p["id"],
            p["waiting"],
            p["turnaround"]))

        total_wait += p["waiting"]
        total_turn += p["turnaround"]

    n = len(results)

    print("\nAverage Waiting Time :", round(total_wait/n,2))
    print("Average Turnaround   :", round(total_turn/n,2))


# ---------------------------------------------------------
# FCFS
# ---------------------------------------------------------
def fcfs(processes):

    procs = sorted(processes,
                   key=lambda x: (x["arrival"]))

    time = 0
    results = []

    for p in procs:

        if time < p["arrival"]:
            time = p["arrival"]

        waiting = time - p["arrival"]

        time += p["burst"]

        turnaround = waiting + p["burst"]

        results.append({
            "id": p["id"],
            "waiting": waiting,
            "turnaround": turnaround
        })

    return results


# ---------------------------------------------------------
# SJF Non Preemptive
# ---------------------------------------------------------
def sjf(processes):

    processes = processes.copy()

    finished = []

    ready = []

    time = 0

    while len(finished) < len(processes):

        for p in processes:
            if p not in ready and p not in finished and p["arrival"] <= time:
                ready.append(p)

        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: (x["burst"], x["arrival"]))

        current = ready.pop(0)

        waiting = time - current["arrival"]

        time += current["burst"]

        turnaround = waiting + current["burst"]

        finished.append({
            "id": current["id"],
            "waiting": waiting,
            "turnaround": turnaround
        })

    return finished


# ---------------------------------------------------------
# Round Robin
# ---------------------------------------------------------
def round_robin(processes, quantum):

    n = len(processes)

    remaining = {}

    for p in processes:
        remaining[p["id"]] = p["burst"]

    completed = {}

    ready = deque()

    time = 0

    arrived = set()

    while len(completed) < n:

        for p in processes:
            if p["arrival"] <= time and p["id"] not in arrived:
                ready.append(p)
                arrived.add(p["id"])

        if not ready:
            time += 1
            continue

        current = ready.popleft()

        run = min(quantum,
                  remaining[current["id"]])

        time += run

        remaining[current["id"]] -= run

        for p in processes:
            if p["arrival"] <= time and p["id"] not in arrived:
                ready.append(p)
                arrived.add(p["id"])

        if remaining[current["id"]] > 0:

            ready.append(current)

        else:

            turnaround = time - current["arrival"]

            waiting = turnaround - current["burst"]

            completed[current["id"]] = {
                "id": current["id"],
                "waiting": waiting,
                "turnaround": turnaround
            }

    return list(completed.values())


# ------------------------------
# Main
# ------------------------------
if __name__ == "__main__":

    processes = load_processes("processes.csv")

    fcfs_results = fcfs(processes)
    sjf_results = sjf(processes)
    rr_results = round_robin(processes, 2)

    print_results("FCFS", fcfs_results)
    print_results("SJF", sjf_results)
    print_results("ROUND ROBIN (Q=2)", rr_results)
