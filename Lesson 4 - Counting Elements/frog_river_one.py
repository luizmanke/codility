#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(X, A):
    time = -1
    leaf_count = 0
    has_leaf = [0 for _ in range(X)]
    for i, leaf_position in enumerate(A):
        if not has_leaf[leaf_position - 1]:
            has_leaf[leaf_position - 1] = 1
            leaf_count += 1
        if leaf_count == X:
            time = i
            break
    return time


if __name__ == "__main__":

    CASES = [
        (5, [1, 3, 1, 4, 2, 3, 5, 4]),
        (10, [1, 3, 1, 4, 2, 3, 5, 4]),
        (100000, range(100000))
    ]

    for position, input_list in CASES:
        print(f"position: {position}")
        print(f"input_list: {input_list}")
        output = solution(position, input_list)

        print(f"output: {output}")
        print("")
