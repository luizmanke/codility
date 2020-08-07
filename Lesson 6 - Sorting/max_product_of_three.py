#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):

    # Select possible values
    sorted_values = sorted(A)
    if len(sorted_values) > 6:
        selected_values = sorted_values[:3] + sorted_values[-3:]
    else:
        selected_values = sorted_values

    # Loop indexes
    maximum_product = float("-inf")
    array_length = len(selected_values)
    for i in range(0, array_length-2):

        # Get P value
        P = selected_values[i]

        # Get Q value
        for j in range(i+1, array_length-1):
            Q = selected_values[j]

            # Get R value
            sub_product = P * Q
            if sub_product >= 0:
                R = max(selected_values[j+1:])
            else:
                R = min(selected_values[j+1:])

            # Compute product
            product = sub_product * R
            if product > maximum_product:
                maximum_product = product

    return maximum_product


if __name__ == "__main__":

    CASES = [
        [-3, 1, 2, -2, 5, 6],
        [1, 2, 3],
        [3, 2, 1],
        [-30, -20, -1, 2, 3, 5],
        [-2, -2, -2, 1, 1, 1],
        list(range(100000))
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
