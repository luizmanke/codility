#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    total_length = len(A)

    # Compute cumulative sums
    first_sums = [0] * total_length
    second_sums = [0] * total_length
    for i in range(1, total_length):

        first_sum = first_sums[i-1] + A[i]
        if first_sum > 0:
            first_sums[i] = first_sum

        second_sum = second_sums[total_length-i] + A[-i-1]
        if second_sum > 0:
            second_sums[total_length-i-1] = second_sum

    # Compute maximum sum
    maximum_sum = 0
    for i in range(1, total_length-1):
        current_sum = first_sums[i-1] + second_sums[i+1]
        if current_sum > maximum_sum:
            maximum_sum = current_sum

    return maximum_sum


if __name__ == "__main__":

    CASES = [
        # [3, 2, 6, 1, 4, 5, 1, 2],
        [3, 2, 6, -1, 4, 5, -1, 2],
        range(100000)
    ]

    for input_array in CASES:
        print(f"input_array: {input_array}")
        output = solution(input_array)

        print(f"output: {output}")
        print("")
