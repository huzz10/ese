#!/usr/bin/env python3 

def sstf(tracks):
    n = len(tracks)
    total_diff = 0
    current_position = tracks[0]
    unprocessed_tracks = tracks[1:]  # Remaining tracks after the starting track
    order_of_processing = [current_position]

    while unprocessed_tracks:
        # Find the closest track
        closest_track = min(unprocessed_tracks, key=lambda x: abs(x - current_position))
        total_diff += abs(closest_track - current_position)
        current_position = closest_track
        unprocessed_tracks.remove(closest_track)
        order_of_processing.append(current_position)

    print(f"Order of processing: {order_of_processing}")
    print(f"Total Seek Time: {total_diff}")
    print(f"Average Seek Time: {total_diff / (n - 1)}")
    print()


# Example usage
tracks = [100, 50, 10, 200, 150]
sstf(tracks)
