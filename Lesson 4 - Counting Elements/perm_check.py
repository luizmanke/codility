#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    A = sorted(A)
    permutation = 1
    count = 1
    for number in A:
        if number != count:
            permutation = 0
            break
        count += 1
    return permutation


if __name__ == "__main__":

    CASES = [
        [4, 1, 3, 2],
        [4, 1, 3],
        range(1, 100000)
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
