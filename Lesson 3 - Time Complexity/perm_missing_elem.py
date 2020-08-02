"""
An array A consisting of N different integers is given. The array contains integers
in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:
    def solution(A)
that, given an array A, returns the value of the missing element.

For example, given array A such that:
    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:
    - N is an integer within the range [0..100,000];
    - the elements of A are all distinct;
    - each element of array A is an integer within the range [1..(N + 1)].
"""


def solution(A):
    A = sorted(A)
    i = 0
    while i < len(A):
        if i + 1 != A[i]:
            break
        i += 1
    return i + 1


if __name__ == "__main__":

    CASES = [
        [2, 3, 1, 5],
        [],
        [1],
        [2, 3, 4],
        [1, 2, 3]
    ]

    for input_list in CASES:
        print(f"input_list: {input_list}")
        output = solution(input_list)

        print(f"output: {output}")
        print("")
