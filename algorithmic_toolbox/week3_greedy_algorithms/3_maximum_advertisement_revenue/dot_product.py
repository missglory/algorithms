#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    n = len(a)
    while n > 0:
        if a[n - 1] > 0:
            res += a.pop() * b.pop()
        else:
            res += a.pop(0) * b.pop(0)
        n = len(a)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    a.sort()
    b.sort()
    print(max_dot_product(a, b))
    
