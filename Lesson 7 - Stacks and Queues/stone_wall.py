#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(H):
    n_stones = 0
    stack = []

    for i in range(len(H)):

        # Remove tall walls
        while len(stack) > 0 and H[i] < stack[-1]:
            stack.pop()

        # Add one stone
        if len(stack) == 0 or H[i] != stack[-1]:
            n_stones += 1
            stack.append(H[i])

    return n_stones


if __name__ == "__main__":

    CASES = [
        [1, 2, 3, 4],
        [1, 2, 1, 2],
        [4, 3, 2, 1],
        [3, 2, 1, 3, 2],
        [8, 8, 5, 7, 9, 8, 7, 4, 8],
        list(range(1, 50000)) + list(range(50000, 1, -1))
    ]

    for input_hights in CASES:
        print(f"input_hights: {input_hights}")
        output = solution(input_hights)

        print(f"output: {output}")
        print("")
