#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A):
    A = sorted(A)
    count = 1
    for number in A:
        if number > count - 1:
            if number != count:
                break
            count += 1
    return count


if __name__ == "__main__":

    CASES = [
        [1, 3, 6, 4, 1, 2],
        [1, 2, 3],
        [-1, -3],
        range(50000, -50000, -1)
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
