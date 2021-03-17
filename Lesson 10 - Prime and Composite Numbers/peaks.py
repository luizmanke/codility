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

    # Find maximum number of blocks
    max_blocks = 0
    array = [i for i in range(len(A))]
    for n_blocks in range(len(peaks), 0, -1):

        # Check if array is divisible
        if len(A) % n_blocks == 0:
            incorrect = False
            block_size = int(len(A) / n_blocks)

            # Check if blocks contain peaks
            for i in range(n_blocks):
                current_block = array[i*block_size:(i+1)*block_size]
                peaks_in_block = list(map(lambda peak: peak in current_block, peaks))
                if sum(peaks_in_block) == 0:
                    incorrect = True
                    break

            # If not incorrect, return maximum blocks found
            if not incorrect:
                max_blocks = n_blocks
                break

    return max_blocks


if __name__ == '__main__':

    CASES = [
        [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    ]

    for array in CASES:
        print(f'input: {array}')
        output = solution(array)

        print(f'output: {output}')
        print('')
