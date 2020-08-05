#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    A = sorted(A)
    i = 0
    while i+1 < len(A):
        if A[i] == A[i+1]:
            i += 2
        else:
            break
    return A[i]


if __name__ == "__main__":

    CASES = [
        [9, 3, 9, 3, 9, 7, 9]
    ]

    for input_list in CASES:
        print(f"input: {input_list}")
        result = solution(input_list)

        print(f"output: {result}")
        print("")
