#!/usr/bin/env python3 

def calculate_need(max_matrix, allocation_matrix):
    """
    Calculate the Need matrix as Max - Allocation.
    """
    rows = len(max_matrix)
    cols = len(max_matrix[0])
    need_matrix = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            need_matrix[i][j] = max_matrix[i][j] - allocation_matrix[i][j]
    
    return need_matrix


def is_safe_state(available, max_matrix, allocation_matrix):
    """
    Check if the system is in a safe state and determine the safe sequence.
    """
    need_matrix = calculate_need(max_matrix, allocation_matrix)
    work = available[:]  # Copy of available resources
    finish = [False] * len(max_matrix)  # Track if a process is finished
    safe_sequence = []
    
    while len(safe_sequence) < len(max_matrix):
        found = False
        for i in range(len(max_matrix)):
            if not finish[i] and all(need_matrix[i][j] <= work[j] for j in range(len(work))):
                # Process i can be completed
                for j in range(len(work)):
                    work[j] += allocation_matrix[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True
                break
        
        if not found:
            return False, []  # System is not in a safe state
    
    return True, safe_sequence


def bankers_algorithm():
    # Input: Available resources, Max matrix, and Allocation matrix
    available = [3, 3, 2]
    max_matrix = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    allocation_matrix = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    
    is_safe, safe_sequence = is_safe_state(available, max_matrix, allocation_matrix)
    
    if is_safe:
        print("The system is in a safe state.")
        print(f"Safe sequence: {safe_sequence}")
    else:
        print("The system is not in a safe state.")


if __name__ == "__main__":
    bankers_algorithm()

