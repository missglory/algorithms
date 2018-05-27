# Uses python3
import sys


def get_change(m):
    res = m // 10
    res += (m  % 10) // 5
    res += ((m  % 10) % 5)
    return res

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))
