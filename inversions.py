array = open("IntegerArray.txt").read().split()

def inversions(array):
    n = len(array)
    if n == 1:
        return array, 0
    else:

        (x, left_inv) = inversions(array[:n//2])
        (y, right_inv) = inversions(array[n//2:])
        (z, split_inv) = split_inversions(x, y)

    return z, left_inv + right_inv + split_inv

def split_inversions(b, C):

    D = []
    split_inv = 0
    x = len(b)
    y = len(C)
    i = 0
    j = 0
    k = len(b) + len(C)
    for q in range(k):

        if b[i] < C[j]:
            D += [b[i]]
            i += 1
        elif b[i] >= C[j]:
            D += [C[j]]
            j += 1
            split_inv += len(b[i:])
        if i == len(b):
            D += C[j:]
            return D, split_inv
        if j == len(C):
            D += b[i:]
            return D, split_inv


sort_arr, answer = inversions(array)
print(answer)
