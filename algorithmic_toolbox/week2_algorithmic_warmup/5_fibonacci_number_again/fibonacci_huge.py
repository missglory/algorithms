# Uses python3
import sys


arr = [0] * (int)(1e5 + 2)
arr[:3] = [0,1,1]

def get_fibonacci_huge_naive(n, m):
    if n <= 3:
        return arr[n]

    for i in range(3, min(n + 1, 10 * m + 1)):
        # previous, current = current, previous + current
        arr[i] = arr[i-1] + arr[i -2 ]
        arr[i] %= m

    return arr[m]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
    print('arr\n', arr[:5*m])
    print(arr.f)