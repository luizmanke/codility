#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    has_triplet = 0

    A = sorted(A)
    for i in range(2, len(A)):
        if A[i-2] + A[i-1] > A[i]:
            has_triplet = 1
            break

    return has_triplet


if __name__ == "__main__":

    CASES = [
        [10, 2, 5, 1, 8, 20],
        [10, 50, 5, 1],
        [2] * 100000
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
