#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(S):
    is_nested = 1

    total_brackets = 0
    for bracket in S:

        if bracket == "(":
            total_brackets += 1
        elif total_brackets > 0:
            total_brackets -= 1
        else:
            is_nested = 0
            break

    if total_brackets != 0:
        is_nested = 0

    return is_nested


if __name__ == "__main__":

    CASES = [
        "(()(())())",
        "())",
        "(" * 500000 + ")" * 500000
    ]

    for input_string in CASES:
        print(f"input_string: {input_string}")
        output = solution(input_string)

        print(f"output: {output}")
        print("")
