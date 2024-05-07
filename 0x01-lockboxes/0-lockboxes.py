#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Keeps track of visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = [0]  # Initialize the queue with the first box

    while queue:
        current_box = queue.pop(0)  # Get the next box from the queue
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a box that hasn't been visited yet
            if 0 <= key < n and not visited[key]:
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue

    # If all boxes have been visited, return True, else return False
    return all(visited)
