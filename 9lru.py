#!/usr/bin/env python3 

def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0
    page_usage = {}  # Tracks when pages were last used

    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Find the least recently used page
                lru_page = min(page_usage, key=page_usage.get)
                memory.remove(lru_page)
                memory.append(page)
                del page_usage[lru_page]
        page_usage[page] = i
        print(f"Memory: {memory}, Page Usage: {page_usage}")

    print(f"Total Page Faults (LRU): {page_faults}")


# Example usage for LRU
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
lru_page_replacement(pages, capacity)
