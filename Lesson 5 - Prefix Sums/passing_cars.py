#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    n_passing_cars = 0

    # Remove 1s to the right
    try:
        first_zero_index = A.index(0)
        A = A[first_zero_index:]
    except Exception:
        return 0

    # Loop backwards
    count = 0
    cars_left = len([x for x in A if x == 0])
    for i in range(len(A)-1, -1, -1):
        if A[i] != 0:
            count += 1
        else:
            n_passing_cars += count * cars_left
            cars_left -= 1
            count = 0

        # Check if number exceeds 1,000,000,000
        if n_passing_cars > 1000000000:
            n_passing_cars = -1
            break

    return n_passing_cars


if __name__ == "__main__":

    CASES = [
        [0, 1],
        [1, 0],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 1] * 50000
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
