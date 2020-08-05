#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(N):

    # Integer to binary
    binary = bin(N)
    binary = binary[2:]

    # Remove zeros on the right
    while binary[-1] == "0":
        binary = binary[:-1]

    # Get list of gaps
    list_of_gaps = binary.split("1")

    # Count
    count = [len(gap) for gap in list_of_gaps]

    return max(count)


if __name__ == "__main__":

    CASES = [
        1041,
        15,
        32
    ]

    for integer in CASES:
        print(f"input: {integer}")
        result = solution(integer)

        print(f"output: {result}")
        print("")
