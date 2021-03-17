import math

def solution(N):

    square_root = math.sqrt(N)
    maximum_A = int(square_root)
    for A in range(maximum_A, 0, -1):
        if N % A == 0:
            B = N / A
            break

    minimum_perimeter = int(2 * (A + B))

    return minimum_perimeter


if __name__ == '__main__':

    CASES = [
        30,
        50
    ]

    for array in CASES:
        print(f'input: {array}')
        output = solution(array)

        print(f'output: {output}')
        print('')
