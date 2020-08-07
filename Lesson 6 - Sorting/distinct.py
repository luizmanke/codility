#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    unique_values = set(A)
    n_unique_values = len(unique_values)
    return n_unique_values


if __name__ == "__main__":

    CASES = [
        [2, 1, 1, 2, 3, 1],
        list(range(100000))
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
