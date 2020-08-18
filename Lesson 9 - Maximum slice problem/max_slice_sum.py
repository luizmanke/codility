#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):

    current_sum = A[0]
    maximum_sum = A[0]
    for value in A[1:]:
        next_sum = current_sum + value

        if next_sum > current_sum or next_sum > 0:
            current_sum = next_sum
        else:
            current_sum = value

        if value > current_sum:
            current_sum = value

        if current_sum > maximum_sum:
            maximum_sum = current_sum

    return maximum_sum


if __name__ == "__main__":

    CASES = [
        [5],
        [1, 3],
        [-2, 1],
        [-2, 3],
        [3, -2, 3],
        [3, 2, -6, 4, 0],
        [-100, -100, -100],
        range(1000000)
    ]

    for input_array in CASES:
        print(f"input_array: {input_array}")
        output = solution(input_array)

        print(f"output: {output}")
        print("")
