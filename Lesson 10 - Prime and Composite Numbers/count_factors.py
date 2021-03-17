def solution(N):
    n_factors = 0

    i = 1
    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                n_factors += 1
            else:
                n_factors += 2
        i += 1

    return n_factors


if __name__ == '__main__':

    CASES = [
        1,
        24,
        2147483647
    ]

    for number in CASES:
        print(f'input: {number}')
        output = solution(number)

        print(f'output: {output}')
        print('')
