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
