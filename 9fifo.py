#!/usr/bin/env python3 

def fifo_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    pointer = 0  # Pointer to replace pages in a FIFO manner

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % capacity
        print(f"Memory: {memory}")

    print(f"Total Page Faults (FIFO): {page_faults}")


# Example usage for FIFO
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
fifo_page_replacement(pages, capacity)
