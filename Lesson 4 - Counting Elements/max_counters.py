#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(N, A):
    is_maximized = True
    maximum = 0
    array = [0] * N
    for index in A:

        # Increment
        if index <= N:
            new_value = array[index - 1] + 1
            array[index - 1] = new_value

            # Update maximum value
            if new_value > maximum:
                maximum = new_value
                is_maximized = False

        # Maximize
        elif not is_maximized:
            array = [maximum] * N
            is_maximized = True

    return array


if __name__ == "__main__":

    CASES = [
        (5, [3, 4, 4, 6, 1, 4, 4]),
        (100000, range(50000, 150000))
    ]

    for n_counters, operations in CASES:
        print(f"n_counters: {n_counters}")
        print(f"operations: {operations}")
        output = solution(n_counters, operations)

        print(f"output: {output}")
        print("")
