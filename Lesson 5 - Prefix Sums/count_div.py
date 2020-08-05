#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solution(A, B, K):

    # Check if K is below B
    if K > B:
        if B == 0:
            return 1
        else:
            return 0

    # Eliminate impossible numbers
    if K > A and A != 0:
        A = K

    # Find first divisible number
    for number in range(A, B+1):
        if number % K == 0:
            first_divisible_numbers = number
            break

    # Find last divisible number
    for number in range(B, A-1, -1):
        if number % K == 0:
            last_divisible_numbers = number
            break

    # Count
    try:
        count = 1 + ((last_divisible_numbers - first_divisible_numbers) / K)
    except Exception:
        count = 0

    return int(count)


if __name__ == "__main__":

    CASES = [
        (6, 11, 2),
        (0, 0, 2),
        (2, 2, 2),
        (0, 5, 15),
        (0, 2000000000, 1)
    ]

    for start_number, end_number, divisor in CASES:
        print(f"start_number: {start_number}")
        print(f"end_number: {end_number}")
        print(f"divisor: {divisor}")
        output = solution(start_number, end_number, divisor)

        print(f"output: {output}")
        print("")
