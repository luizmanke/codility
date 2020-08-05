#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):

    # Compute for P == 1
    P = 1
    sum_before = sum(A[:P])
    sum_after = sum(A[P:])
    difference = abs(sum_before - sum_after)

    for P in range(2, len(A)):
        sum_before = sum_before + A[P-1]
        sum_after = sum_after - A[P-1]
        new_difference = abs(sum_before - sum_after)
        if new_difference < difference:
            difference = new_difference

    return difference


if __name__ == "__main__":

    CASES = [
        [3, 1, 2, 4, 3],
        [1, 1],
        [1, 2, 3],
        [1, 2, 3, 4, 5],
        [-3, -2, -1, 0, 1, 2, 3]
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
