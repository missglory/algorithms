# Uses python3
import sys
import random

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    m = (left + right)//2
    while left+1 < right:
        try:
            if x == a[m]: return m
            if x < a[m]:
                right = m
                m = (left + right) // 2
                continue
            if x > a[m]:
                left = m + 1
                m = (left + right) // 2
                continue
        except IndexError:
            raise IndexError(left, right, m)
        raise Exception(left, right, m)
    if left > len(a) - 1: return - 1
    if not x == a[left]: return -1
    return left

    # return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    # while True:
        # n = random.randint()
        # m = 
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
