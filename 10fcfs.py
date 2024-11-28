#!/usr/bin/env python3 

def fcfs(tracks):
    n = len(tracks)
    total_diff = 0

    print(f"Order of processing: {tracks}")
    for i in range(n - 1):
        total_diff += abs(tracks[i + 1] - tracks[i])

    print(f"Total Seek Time: {total_diff}")
    print(f"Average Seek Time: {total_diff / (n - 1)}")
    print()


# Example usage
tracks = [100, 50, 10, 200, 150]
fcfs(tracks)
