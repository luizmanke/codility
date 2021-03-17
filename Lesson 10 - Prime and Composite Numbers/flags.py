def solution(A):

    # Find peaks
    i = 1
    peaks = []
    while i <= len(A)-1:
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
            i += 2
        else:
            i += 1

    # Find maximum number of flags
    max_flags = 0
    for n_flags in range(len(peaks), 0, -1):
        count = 1
        previous_peak = 0
        for i in range(1, n_flags):
            if peaks[i] - peaks[previous_peak] >= n_flags:
                previous_peak = i
                count += 1
        if count > max_flags:
            max_flags = count

    return max_flags


if __name__ == '__main__':

    CASES = [
        [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    ]

    for array in CASES:
        print(f'input: {array}')
        output = solution(array)

        print(f'output: {output}')
        print('')
