# Uses python3
import sys
import itertools

width = (int)(7e2 + 5)
height = 22
arr = [[0] * width for x in range(height)]

def optimal_weight(W, w):
    n = len(w)
    # print('WEIGHT', W, 'NUM_ELEMS', n)
    for i in range(1, n + 1):
        arr[i] = arr[i-1][:]
        for j in range(1, W + 1):
            if j < w[i - 1]:
                continue
            try: arr[i][j] = max(arr[i][j], arr[i-1][j - w[i - 1]] + w[i - 1])
            except IndexError:
                raise Exception(i,j, w[i - 1])
    return arr[n][W]

# def print_arr(): pass
def print_arr():
    for x in arr:
        for y in x:
            sys.stdout.write(str(y) + '\t')
        sys.stdout.write('\n')



def partition3(A):
    n = len(A)
    sumA = sum(A)
    if not sumA % 3 == 0:
        return 0
    optimal_weight(sumA // 3, A)
    # print_arr()
    i = n
    j = sumA // 3
    count = 0
    for i in range(1,n+1):
        if arr[i][j] == j:
            count += 1
    if count >= 3:
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

