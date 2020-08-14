#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    dominator_index = -1
    half = len(A) / 2
    check_in = {}

    for i in range(len(A)):
        number = A[i]

        try:
            check_in[number]["count"] += 1
            check_in[number]["list"].append(i)
        except Exception:
            check_in[number] = {
                "count": 1,
                "list": [i]
            }

        if check_in[number]["count"] > half:
            dominator_index = check_in[number]["list"][0]
            break

    return dominator_index


if __name__ == "__main__":

    CASES = [
        [],
        [3, 4, 3, 2, 3, -1, 3, 3],
        range(100000),
        [1] * 100000
    ]

    for input_array in CASES:
        print(f"input_array: {input_array}")
        output = solution(input_array)

        print(f"output: {output}")
        print("")
