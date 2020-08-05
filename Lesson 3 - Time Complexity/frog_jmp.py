#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# System packages
import math


def solution(X, Y, D):
    distance = Y - X
    steps = math.ceil(distance / D)
    return steps


if __name__ == "__main__":

    CASES = [
        (10, 85, 30)
    ]

    for initial_position, final_position, step_length in CASES:
        print(f"initial_position: {initial_position}")
        print(f"final_position: {final_position}")
        print(f"step_length: {step_length}")
        output = solution(initial_position, final_position, step_length)

        print(f"output: {output}")
        print("")