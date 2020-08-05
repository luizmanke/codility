#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    A = sorted(A)
    i = 0
    while i < len(A):
        if i + 1 != A[i]:
            break
        i += 1
    return i + 1


if __name__ == "__main__":

    CASES = [
        [2, 3, 1, 5],
        [],
        [1],
        [2, 3, 4],
        [1, 2, 3]
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
