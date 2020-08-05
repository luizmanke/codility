#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(S, P, Q):
    queries = []
    for i in range(len(P)):
        sliced = S[P[i]:Q[i] + 1]
        if "A" in sliced:
            minimum = 1
        elif "C" in sliced:
            minimum = 2
        elif "G" in sliced:
            minimum = 3
        elif "T" in sliced:
            minimum = 4
        queries.append(minimum)
    return queries


if __name__ == "__main__":

    CASES = [
        ("CAGCCTA", [2, 5, 0, 0], [4, 5, 6, 0]),
        ("A"*80000, [2] * 50000, [60000] * 50000)
    ]

    for dna_string, P, Q in CASES:
        print(f"dna_string: {dna_string}")
        print(f"P: {P}")
        print(f"Q: {Q}")
        output = solution(dna_string, P, Q)

        print(f"output: {output}")
        print("")
