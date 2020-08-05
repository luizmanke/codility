#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# System packages
import random


def solution(A):
    minimum_p = float("inf")
    minimum_avg = float("inf")

    # Calculate for 2 samples
    for p in range(0, len(A)-1):
        avg = sum(A[p:p+2]) / 2
        if avg < minimum_avg or ((avg == minimum_avg) and p < minimum_p):
            minimum_p = p
            minimum_avg = avg

    # Calculate for 3 samples
    for p in range(0, len(A)-2):
        avg = sum(A[p:p+3]) / 3
        if avg < minimum_avg or ((avg == minimum_avg) and p < minimum_p):
            minimum_p = p
            minimum_avg = avg

    return minimum_p


if __name__ == "__main__":

    CASES = [
        [4, 2, 2, 5, 1, 5, 8],
        [random.randint(-10000, 10000) for _ in range(100000)]
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
