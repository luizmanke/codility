#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# System packages
from bisect import bisect_right


def solution(A):
    n_intersections = 0

    min_disc_values = [position - radius for position, radius in enumerate(A)]
    min_disc_values = sorted(min_disc_values)

    for position, radius in enumerate(A):
        max_disc_value = position + radius
        count_of_intersections = bisect_right(min_disc_values, max_disc_value)
        n_intersections += count_of_intersections - position - 1

    # Check if the number of intersections exceeded
    if n_intersections > 10000000:
        n_intersections = -1

    return n_intersections


if __name__ == "__main__":

    CASES = [
        [1, 5, 2, 1, 4, 0],
        [2] * 100000
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
