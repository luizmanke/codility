#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A, K):
    if A:
        for _ in range(K):
            A = [A[-1]] + A[:-1]
    return A


if __name__ == "__main__":

    CASES = [
        ([3, 8, 9, 7, 6], 3),
        ([0, 0, 0], 1),
        ([1, 2, 3, 4], 4)
    ]

    for input_list, n_shifts in CASES:
        print(f"list: {input_list}")
        print(f"n_shifts: {n_shifts}")
        result = solution(input_list, n_shifts)

        print(f"output: {result}")
        print("")
