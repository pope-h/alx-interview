#!/usr/bin/python3
""" Defines lockboxes """


def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
