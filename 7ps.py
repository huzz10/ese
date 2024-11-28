#!/usr/bin/env python3 

def priority_scheduling(processes):
    # Sort processes by priority, then by arrival time
    processes.sort(key=lambda x: (x['priority'], x['arrival']))
    time = 0
    for process in processes:
        process['start'] = max(time, process['arrival'])
        process['finish'] = process['start'] + process['burst']
        time = process['finish']
    for process in processes:
        process['turnaround'] = process['finish'] - process['arrival']
        process['waiting'] = process['turnaround'] - process['burst']
    return processes

# User-defined input
n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    print(f"\nEnter details for Process {i + 1}:")
    pid = i + 1
    arrival = int(input("Arrival Time: "))
    burst = int(input("Burst Time: "))
    priority = int(input("Priority (lower number = higher priority): "))
    processes.append({'id': pid, 'arrival': arrival, 'burst': burst, 'priority': priority})

# Run Priority scheduling
scheduled = priority_scheduling(processes)

# Display results
print("\nProcess Details After Priority Scheduling:")
print(f"{'ID':<5}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Start':<10}{'Finish':<10}{'Turnaround':<12}{'Waiting':<10}")
for process in scheduled:
    print(f"{process['id']:<5}{process['arrival']:<10}{process['burst']:<10}{process['priority']:<10}"
          f"{process['start']:<10}{process['finish']:<10}{process['turnaround']:<12}{process['waiting']:<10}")

