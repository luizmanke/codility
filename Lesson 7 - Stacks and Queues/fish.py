#!/usr/bin/env python3
# -*- coding: utf-8 -*-

UPSTREAM = 0
DOWNSTREAM = 1


def solution(A, B):

    fishs = []
    for i in range(len(A)):
        new_fish = (A[i], B[i])

        while len(fishs) > 0:

            if new_fish[1] == UPSTREAM and fishs[-1][1] == DOWNSTREAM:
                if new_fish[0] > fishs[-1][0]:
                    del fishs[-1]
                else:
                    break

            else:
                fishs.append(new_fish)
                break

        if len(fishs) == 0:
            fishs.append(new_fish)

    return len(fishs)


if __name__ == "__main__":

    CASES = [
        ([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]),
        (list(range(999900000, 1000000000)), [0, 1] * 50000)
    ]

    for sizes, directions in CASES:
        print(f"sizes: {sizes}")
        print(f"directions: {directions}")
        output = solution(sizes, directions)

        print(f"output: {output}")
        print("")
