#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def solution(S):
    is_nested = 1

    pseudo_S = ""
    for bracket in S:

        if bracket in PAIRS:
            pseudo_S += bracket
        elif pseudo_S == "":
            is_nested = 0
            break
        elif bracket == PAIRS[pseudo_S[-1]]:
            pseudo_S = pseudo_S[:-1]
        else:
            is_nested = 0
            break

    if pseudo_S != "":
        is_nested = 0

    return is_nested


if __name__ == "__main__":

    CASES = [
        "",
        "{[()()]}",
        "()()])",
        "([)()]",
        "(" * 200000,
        "{" * 100000 + "}" * 100000
    ]

    for input_string in CASES:
        print(f"input_string: {input_string}")
        output = solution(input_string)

        print(f"output: {output}")
        print("")
