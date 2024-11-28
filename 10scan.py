#!/usr/bin/env python3 

def scan(tracks, disk_size, direction):
    n = len(tracks)
    total_diff = 0
    current_position = tracks[0]
    sorted_tracks = sorted(tracks[1:])  # Exclude starting track and sort

    if direction == "left":
        left = [t for t in sorted_tracks if t < current_position]
        right = [t for t in sorted_tracks if t >= current_position]
    else:
        left = [t for t in sorted_tracks if t < current_position]
        right = [t for t in sorted_tracks if t >= current_position]
        left, right = right, left  # Process right first, then left

    order_of_processing = [current_position] + right + left[::-1]

    for i in range(len(order_of_processing) - 1):
        total_diff += abs(order_of_processing[i + 1] - order_of_processing[i])

    print(f"Order of processing: {order_of_processing}")
    print(f"Total Seek Time: {total_diff}")
    print(f"Average Seek Time: {total_diff / (n - 1)}")
    print()


# Example usage
tracks = [100, 50, 10, 200, 150]
disk_size = 300
scan(tracks, disk_size, direction="left")
