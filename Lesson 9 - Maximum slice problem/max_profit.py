#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):

    # Compute differences
    differences = [0] * (len(A) - 1)
    for i in range(len(A) - 1):
        differences[i] = A[i+1] - A[i]

    # Cumulative sum
    maximum_profit = 0
    cumulative_sum = [0] * len(differences)
    for i in range(len(differences)):
        profit = cumulative_sum[i-1] + differences[i]

        if profit > 0:
            cumulative_sum[i] = profit

        if profit > maximum_profit:
            maximum_profit = profit

    return maximum_profit


if __name__ == "__main__":

    CASES = [
        [23171, 21011, 21123, 21366, 21013, 21367],
        range(400000)
    ]

    for input_array in CASES:
        print(f"input_array: {input_array}")
        output = solution(input_array)

        print(f"output: {output}")
        print("")
