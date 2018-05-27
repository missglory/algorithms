# Uses python3
import sys
width = (int)(1e4 + 5)
height = 303
arr = [[0] * width for x in range(height)]

def print_arr():
    pass

def print_arr2():
    for x in arr:
        for y in x:
            sys.stdout.write(str(y) + '\t')
        sys.stdout.write('\n')

def optimal_weight(W, w):
    n = len(w)
    for i in range(1, n + 1):
        arr[i] = arr[i-1][:]
        for j in range(1, W + 1):
            if j < w[i - 1]:
                continue
            arr[i][j] = max(arr[i][j], arr[i-1][j - w[i - 1]] + w[i - 1])
    
    return arr[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print_arr()
    print(optimal_weight(W, w))
    print_arr()
