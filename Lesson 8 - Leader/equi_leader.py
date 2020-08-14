#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    n_equi_leaders = 0
    total_length = len(A)

    # Create right handler
    right_handler = {}
    for number in A:
        count = right_handler.get(number, 0)
        right_handler[number] = count + 1

    # Loop numbers
    leader = A[0]
    left_handler = {}
    for i in range(len(A)):
        number = A[i]

        # Update handlers
        count = left_handler.get(number, 0)
        left_handler[number] = count + 1
        right_handler[number] -= 1

        # Update left leader
        if left_handler[number] > left_handler[leader]:
            leader = number

        # Check for equi leaders
        if left_handler[leader] > (i+1) / 2:
            if right_handler[leader] > (total_length - (i+1)) / 2:
                n_equi_leaders += 1

    return n_equi_leaders


if __name__ == "__main__":

    CASES = [
        [4, 3, 4, 4, 4, 2],
        range(100000),
        [1] * 100000
    ]

    for input_array in CASES:
        print(f"input_array: {input_array}")
        output = solution(input_array)

        print(f"output: {output}")
        print("")
