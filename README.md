# CampusConnect-OS-Assignment

## Scheduling Algorithms

This project implements:

- First Come First Serve (FCFS)
- Shortest Job First (Non-preemptive)
- Round Robin

### Dataset

| Process | Arrival | Burst |
|----------|---------|-------|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |
| P5 | 6 | 6 |

### Tie-breaking Rules

- Earlier arrival time first.
- If arrival time is the same, input order is used.
- For SJF, equal burst times are broken by arrival time and then input order.
- In Round Robin, processes arriving during a time quantum are added to the ready queue before re-enqueuing the preempted process.

The simulator prints the waiting time, turnaround time, average waiting time, and average turnaround time for all three scheduling algorithms.

# Task 2 - Priority Scheduling with Aging

Priority scheduling uses the convention that a **higher numeric value means a higher priority**.

Initial priorities:

| Process | Priority |
|----------|----------|
| P1 | 1 |
| P2 | 5 |
| P3 | 5 |
| P4 | 5 |
| P5 | 5 |

P1 has the lowest priority and would be delayed while higher-priority processes continue to arrive.

To prevent starvation, **aging** is applied every **2 waiting time units**.

Whenever a process waits for 2 units, its priority increases by 1.

Eventually P1 reaches the same priority as the other processes and is scheduled.

## Aging Trace

| Time | P1 Priority | Running Process |
|------|-------------|-----------------|
| 0 | 1 | P2 |
| 2 | 2 | P3 |
| 4 | 3 | P4 |
| 6 | 4 | P5 |
| 8 | 5 | P1 |

Without aging, P1 would continue waiting if new high-priority processes kept arriving. Aging gradually increases its priority until it becomes eligible to run, preventing starvation.

### Starvation Scenario

Assume that after every two time units, a new process with priority 5 arrives. Without aging, P1 (priority 1) would never be selected because there would always be another higher-priority process ready to run.

With aging enabled, P1's priority increases every two waiting units:

1 → 2 → 3 → 4 → 5

Once its priority reaches 5, it is selected according to the scheduling policy, eliminating starvation.


