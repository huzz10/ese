#!/usr/bin/env python3 

def optimal_page_replacement(pages, capacity):
    """
    Implements the Optimal Page Replacement Algorithm.
    :param pages: List of page references.
    :param capacity: Number of frames in memory.
    :return: Number of page faults.
    """
    frames = []  # Memory frames
    page_faults = 0

    for i in range(len(pages)):
        # If the page is not in memory, it causes a page fault
        if pages[i] not in frames:
            if len(frames) < capacity:
                # If there is still space in memory, add the page
                frames.append(pages[i])
            else:
                # Find the page to replace
                farthest = i
                replace_index = -1

                for j in range(len(frames)):
                    # Find the next occurrence of each page in the frame
                    if frames[j] not in pages[i + 1:]:
                        replace_index = j
                        break
                    else:
                        index = pages[i + 1:].index(frames[j])
                        if index > farthest:
                            farthest = index
                            replace_index = j

                # Replace the selected page with the new page
                frames[replace_index] = pages[i]

            page_faults += 1

        # Debugging output (optional)
        print(f"Step {i + 1}: Page {pages[i]} -> Frames: {frames}")

    return page_faults


# Example Usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3  # Number of memory frames
    faults = optimal_page_replacement(pages, capacity)
    print(f"\nTotal Page Faults: {faults}")

