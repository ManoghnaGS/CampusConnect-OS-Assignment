
# Deadlock Analysis

## Scenario

There are three processes:

- P1
- P2
- P3

There are three resource types:

- R1
- R2
- R3

Each resource has one instance.

Current allocation and requests:

- P1 holds R1 and requests R2.
- P2 holds R2 and requests R3.
- P3 holds R3 and requests R1.

This creates a circular wait, so no process can continue.

---

## Resource Allocation Graph

Allocation edges:

R1 → P1

R2 → P2

R3 → P3

Request edges:

P1 → R2

P2 → R3

P3 → R1

Cycle:

P1 → R2 → P2 → R3 → P3 → R1 → P1

The cycle indicates a deadlock because each process is waiting for a resource held by another process in the cycle.

---

## Four Necessary Conditions for Deadlock

### 1. Mutual Exclusion

Each resource can be allocated to only one process at a time.

Example:
R1 is currently allocated to P1.

---

### 2. Hold and Wait

Processes hold allocated resources while requesting additional resources.

Example:

- P1 holds R1 while waiting for R2.
- P2 holds R2 while waiting for R3.
- P3 holds R3 while waiting for R1.

---

### 3. No Preemption

Resources cannot be forcibly taken away from a process.

Each process releases its resource only after finishing execution.

---

### 4. Circular Wait

A circular chain exists.

P1 waits for P2

P2 waits for P3

P3 waits for P1

This completes the deadlock cycle.

---

## Breaking the Deadlock

Remove the request edge:

P3 → R1

Now P3 is no longer waiting for R1.

P3 finishes execution and releases R3.

P2 obtains R3, completes, and releases R2.

Finally, P1 acquires R2 and completes.

The cycle is eliminated.

---

## Deadlock Prevention Strategy

Use a fixed resource ordering.

Example:

All processes must request resources in the order:

R1 → R2 → R3

A process is not allowed to request a lower-numbered resource after acquiring a higher-numbered one.

This prevents circular wait.

---

## Limitation

Resource ordering reduces flexibility.

A process may need to wait longer even when the required resource is available, leading to lower resource utilization.
